from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Any, Union

AllowedParamTypes = Union[str, int, float, bool, list[str], dict[str, str]]

class OutputFormat(BaseModel):
    finished: bool = Field(
        ...,
        description="Whether the task is complete"
    )
    tool_name: str | None = Field(
        None,
        description="Tool name to call. Must be None if finished is True."
    )
    input_parameters: list[AllowedParamTypes] = Field(
        default_factory=list,
        description="Arguments for the tool. Must be empty if finished is True."
    )
    final_answer: str | None = Field(
        None,
        description="Answer to return if finished=True. Must be provided if finished is True."
    )

class Agent:
    def __init__(self, apikey):
        self.old_memory = []
        self.current_run_steps = []
        self.client = OpenAI(api_key=apikey)

    def start_new_task(self, user_input: str):
        self.current_run_steps = [
            {"role": "user", "content": user_input}
        ]

    def add_tool_execution(self, tool_name: str, inputs: list, output: Any):
        self.current_run_steps.append({
            "role": "assistant",
            "content": f"Called tool '{tool_name}' with parameters {inputs}."
        })
        self.current_run_steps.append({
            "role": "user",
            "content": f"Tool '{tool_name}' returned: {str(output)}"
        })

    def finish_task(self, final_answer: str):
        """Görev tamamlandığında mevcut akışı kalıcı hafızaya taşır ve temizler."""
        if self.current_run_steps:
            task_summary = f"User: {self.current_run_steps[0]['content']} | Answer: {final_answer}"
            self.old_memory.append(task_summary)
        
        self.current_run_steps = []

    def send_to_model(self, tools_schema: list):
        memory_context = "\n".join([f"- {m}" for m in self.old_memory]) if self.old_memory else "None"
        
        system_instruction = {
            "role": "system",
            "content": f"""You are a database manager agent.

Available tools:
{tools_schema}

Historical context from past sessions:
{memory_context}

Return a valid OutputFormat object. Focus on the current task sequence."""
        }

        messages = [system_instruction] + self.current_run_steps

        raw_completion = self.client.beta.chat.completions.parse(
            model="gpt-4.1-mini", 
            messages=messages,
            response_format=OutputFormat
        )

        parsed_object = raw_completion.choices[0].message.parsed
        usage_info = raw_completion.usage 

        return parsed_object, usage_info
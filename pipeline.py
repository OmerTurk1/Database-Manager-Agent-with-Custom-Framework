import inspect
import tools

functions_list = inspect.getmembers(tools, inspect.isfunction)

for name, func in functions_list:
    print(f"--- Fonksiyon Adı: {name} ---")
    
    description = inspect.getdoc(func)
    print(f"Açıklama:\n{description if description else 'Açıklama bulunamadı.'}")
    
    print("Parametreler:")
    signature = inspect.signature(func)
    
    if not signature.parameters:
        print("  (Bu fonksiyon parametre almıyor)")
    else:
        for param_name, param in signature.parameters.items():
            
            annotation = f" [{param.annotation.__name__}]" if param.annotation != inspect.Parameter.empty else ""
            default = f" (Varsayılan: {param.default})" if param.default != inspect.Parameter.empty else ""
            
            print(f"  - {param_name}{annotation}{default}")
            
    print("\n" + "="*40 + "\n")
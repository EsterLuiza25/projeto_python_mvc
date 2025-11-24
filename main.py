from views.menu_view import MenuView

def main():
    print("Iniciando Sistema de Biblioteca...")
    print("Conectando ao PostgreSQL...")
    
    try:
        sistema = MenuView()
        sistema.mostrar_menu_principal()
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário. Até logo!")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

if __name__ == "__main__":
    main()
import pandas as pd

def csv_to_contacts(input_csv, output_csv):
    # Ler o arquivo CSV
    df = pd.read_csv(input_csv)
    
    # Verificar se as colunas 'Name' e 'Phone' estão presentes
    if 'Name' not in df.columns or 'Phone' not in df.columns:
        raise ValueError("CSV deve conter as colunas 'Name' e 'Phone'")
    
    # Tratar os números de telefone (remover espaços, caracteres especiais etc.)
    df['Phone'] = df['Phone'].str.replace(r'\D', '', regex=True)
    
    # Criar um novo DataFrame para o formato de contatos
    contacts_df = pd.DataFrame({
        'Name': df['Name'],
        'Phone Number': df['Phone']
    })
    
    # Salvar o arquivo em um formato compatível com contatos de celular
    contacts_df.to_csv(output_csv, index=False)
    print(f"Arquivo de contatos salvo como {output_csv}")

if __name__ == '__main__':
    input_csv = r'C:\Users\Mota\Documents\GitHub\Assemblyspeech\transcricao-app_version_2\Whatsapp-automatigo-siganet\results.csv'
    output_csv = r'C:\Users\Mota\Documents\GitHub\Assemblyspeech\transcricao-app_version_2\Whatsapp-automatigo-siganet\contacts.csv'
    csv_to_contacts(input_csv, output_csv)

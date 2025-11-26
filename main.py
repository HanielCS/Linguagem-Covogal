import sys
import time

class AutomatoCovogal:
    def __init__(self):
        # Definição formal dos componentes do Autômato
        self.estados = {'q0', 'q1', 'q_erro'}
        self.alfabeto = {'A', 'E', 'H', 'N'}
        self.estado_inicial = 'q0'
        self.estados_finais = {'q0'}
        
        # Função de Transição (Tabela Delta)
        # Estrutura: {estado_atual: {caractere_lido: proximo_estado}}
        self.transicoes = {
            'q0': {
                'A': 'q1', 'E': 'q1', 
                'H': 'q0', 'N': 'q0'
            },
            'q1': {
                'A': 'q_erro', 'E': 'q_erro', # Vogal seguida de vogal = erro
                'H': 'q0',     'N': 'q0'      # Vogal seguida de consoante = ok (volta p/ q0)
            },
            'q_erro': {
                # Estado morto: qualquer coisa mantém no erro
                'A': 'q_erro', 'E': 'q_erro', 
                'H': 'q_erro', 'N': 'q_erro'
            }
        }

    def processar_cadeia(self, cadeia):
        estado_atual = self.estado_inicial
        passos = []

        print(f"\n--- Iniciando Simulação para: '{cadeia}' ---")
        print(f"Estado Inicial: {estado_atual}")

        for simbolo in cadeia:
            # Validação de Alfabeto
            if simbolo not in self.alfabeto:
                print(f"ERRO CRÍTICO: Símbolo '{simbolo}' não pertence ao alfabeto!")
                return False

            # Busca a transição na tabela
            if simbolo in self.transicoes[estado_atual]:
                proximo_estado = self.transicoes[estado_atual][simbolo]
                
                # Registra o passo para visualização
                passos.append(f"δ({estado_atual}, {simbolo}) -> {proximo_estado}")

                estado_atual = proximo_estado
            else:
                estado_atual = 'q_erro'

            time.sleep(0.05) 

        # Exibe o caminho percorrido (Trace)
        for passo in passos:
            print("   " + passo)

        print(f"Estado Final: {estado_atual}")
        
        if estado_atual in self.estados_finais:
            return True
        else:
            return False

# Interface do Usuário
def main():
    afd = AutomatoCovogal()
    
    print("\n" + "="*50)
    print("   SIMULADOR DE AFD - LINGUAGEM COVOGAL")
    print("="*50)
    print(f"Estados: {afd.estados}")
    print(f"Alfabeto: {afd.alfabeto}")
    print(f"Finais: {afd.estados_finais}")
    print("-" * 50)

    while True:
        try:
            entrada = input("\nDigite uma cadeia (ou 'SAIR'): ").strip().upper()
            
            if entrada == "SAIR":
                print("Encerrando simulação.")
                break
            
            aceita = afd.processar_cadeia(entrada)
            
            if aceita:
                print(f"\nCADEIA ACEITA (Pertence a L)")
            else:
                print(f"\nCADEIA REJEITADA (Não pertence a L)")
                
        except KeyboardInterrupt:
            print("\nSaindo...")
            sys.exit()

if __name__ == "__main__":
    main()
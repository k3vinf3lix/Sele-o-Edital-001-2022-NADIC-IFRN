class candidato ():
    def __init__ (self, nome, cpf, endereco, data_de_nascimento):
            
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.data_de_nascimento = data_de_nascimento
        
    #formatar o objeto em string
    def str(self) -> str:
        ficha = ("Nome: {}\nCPF: {}\nData de nascimento: {}\nEndereco: {}\nNumero do candidato: {}".format(self.nome,self.cpf_candidato,self.data_nascimento,self.endereco,self.numero_candidato))
        return str(ficha)

a1 = candidato("Joao", 82765496308, "Rua das Cortes", "01/08/1961")
a2 = candidato("Maria", 78912345682, "Av Palacio Bandeirantes", "02/04/1988")
a3 = candidato("Joana", 74125896348, "Rua Maria Conceicao", "05/12/1978")
a4 = candidato("Adriano", 25874196364, "Rua Joao Mateus", "07/04/1951")
# Automaça-o-escala-hospitalar
Automação em Python para transformar escala hospitalar desorganizada em base estruturada para análise em BI.

## Descrição
Este projeto automatiza a transformação de uma planilha de escala hospitalar (formato desorganizado) em uma base estruturada pronta para uso de anaslistas de dados.

## Problema
A planilha original possui:
- Setores misturados no meio dos dados
- Estrutura não padronizada
- Dificuldade para análise

## Solução
O script em Python realiza:
- Limpeza da planilha
- Identificação automática de setores
- Separação de funcionários
- Transformação para formato analítico (long format)
- Exportação para Excel pronto para Power BI

## Tecnologias utilizadas
- Python
- Pandas

## Resultado
Arquivo final estruturado com:
- id
- nome
- setor
- dia
- status
- vínculo
- horário
- CHS
- CHM
- JCT

##  Exemplo
→ Antes (planilha desorganizada)

| MASP | NOME | 1 | 2 | 3 |
|------|------|---|---|---|
| NaN  | ENFERMEIROS DIARISTA |
| 123  | JOÃO | P | P | P |
| 456  | MARIA| F | F | P |
| 789  | JUNIA| P | P | P |

→ Depois (base pronta para análise)

| ID | NOME | SETOR      | DIA | STATUS |
|----|------|------------|-----|--------|
|123 | JOÃO | ENFERMEIRO | 1   | P      |
|456 | MARIA| ENFERMEIRO | 1   | F      |
|789 | JUNIA| ENFERMEIRO | 1   | P      |

## Aprendizados
- Manipulação de dados com Pandas
- Tratamento de dados reais (não estruturados)
- Pensamento analítico
- Automação de processos

---
Projeto desenvolvido por Daysi.


© 2026 Daysi. Todos os direitos reservados.
Este código foi desenvolvido para fins de portfólio e não está autorizado para uso ou reprodução sem permissão.

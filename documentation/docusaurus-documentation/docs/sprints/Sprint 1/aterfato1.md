---
title: Artefato - Negócios
sidebar_position: 1
---
import useBaseUrl from "@docusaurus/useBaseUrl";

# Matriz de avaliação de valor Oceano Azul

&emsp;O conceito de Oceano Azul, desenvolvido por Renée Mauborgne e W. Chan Kim, é uma abordagem inovadora nos negócios, conforme detalhado em seu livro de título correspondente. Ao invés de buscar constantemente superar a concorrência, a proposta central é explorar mercados inexplorados como estratégia primordial.

&emsp;Para implementar essa abordagem, é crucial utilizar ferramentas que possibilitem o monitoramento e a tomada de decisões voltadas para a Inovação de Valor. Entre essas ferramentas, destaca-se a Matriz de Avaliação de Valor, a qual permite que as empresas realizem uma análise detalhada de como cada segmento de seu negócio proporciona valor aos clientes. Essa matriz abrange avaliações criteriosas de fatores como preço, qualidade, segurança e outras características relevantes. Além disso, deve-se diferenciar cada atributo da concorrência por meio das ações Reduzir, Eliminar, Aumentar e Criar.

<p align="center"><b> Tabela 1 - Tabela Matriz de avaliação de valor Oceano Azul </b> </p>

| **Atributos** | **ARM** | **Método tradicional** |
| :-----------: | :-----: |:---------------------: |
| Preço | 5 | 10 |
| Precisão | 9 | 7 |
| Tecnologia | 10 | 5 |
| Segurança | 8 | 5 |
| Praticidade | 9 | 0 |
| Previsibilidade | 9 | 7 |
| Tempo de montagem | 5 | 5 |
| Intervenção humana | 4 | 10 |
| Montagem Manual | 0 | 10 |

<p align="center"><b> Figura Gráfico 1 - Matriz de avaliação de valor Oceano Azul </b> </p>
<div align="center">
  <img src={useBaseUrl("/img/MatrizAvaliacaoOceanoAzul.png")} alt="Tabela"></img>
  <p><b>Fonte:</b> elaborado por Arm </p>
</div>


## Reduzir:

&emsp;**Preço:** Cada robô custa cerca de 32.000 reais. Considerando que este é um gasto único, a longo prazo, essa é uma solução mais econômica. Atualmente, cada auxiliar de farmácia custa 2.500 reais, sendo necessários 10 auxiliares para realizar esse trabalho mensalmente. Assim, o gasto do hospital em um único mês é de 25.000 reais apenas com as montagens dos kits de emergência.

&emsp;**Tempo de Montagem:** O tempo de montagem utilizando o robô é mais rápido do que o método tradicional, mas o maior ganho é economizar o tempo dos auxiliares nessa tarefa ao utilizar o robô.

&emsp;**Intervenção Humana:** O MVP permite que a montagem dos kits seja totalmente automatizada. É necessário apenas que um auxiliar de farmácia configure a disposição dos medicamentos no kit e prepare o material.


## Eliminar:

&emsp;**Montagem Manual:** O MVP permite que a montagem dos kits seja totalmente automatizada, sem a necessidade de interferência externa.

## Aumentar:

&emsp;**Precisão:** A cliente mencionou que é comum ocorrerem erros nas montagens dos kits devido ao desvio de atenção dos auxiliares de farmácia responsáveis pela verificação de qualidade e montagem. Esse tipo de erro seria consideravelmente reduzido, pois o braço robótico segue sempre o mesmo padrão, tornando os erros na montagem casos isolados.

&emsp;**Segurança:** No método tradicional, o contato humano está presente em todas as fases do processo de montagem dos kits, aumentando os riscos de contágio por bactérias. A utilização do robô aumentará a segurança hospitalar, garantindo que o contato humano esteja presente apenas nos momentos essenciais.

&emsp;**Previsibilidade:** O robô não requer manutenção frequente, embora seja essencial para manter o bom funcionamento e a durabilidade do equipamento. Por outro lado, o trabalho manual possui o risco de o trabalhador faltar ao serviço por diversos motivos ou até mesmo ser demitido, gerando a necessidade de grandes mudanças e preocupações.

## Criar:

&emsp;**Praticidade:** O processo atual é pouco prático e consome muito tempo dos auxiliares, que poderiam estar realizando outras tarefas. O MVP torna o processo mais prático para os auxiliares, sendo a presença deles necessária apenas para iniciar e finalizar o processo.

&emsp;Analisando a matriz, observa-se o potencial do projeto para transformar significativamente o processo na farmácia hospitalar, beneficiando diversos pacientes e direcionando o tempo de trabalho dos auxiliares de farmácia para tarefas onde a presença humana é realmente essencial.


# Análise Financeira

&emsp;A análise financeira é fundamental para avaliar a viabilidade de investimento em um projeto considerando os custos, o consumo de tempo e a mudança na qualidade enquanto compara com outras alternativas disponíveis. Nesse estudo, foi feita uma análise comparando o braço mecânico MG400 com o método tradicional e manual de montagem dos kits.

## Análise do custo do método Arm

<p align="center"><b> Tabela 2 - Análise do custo do método Arm </b> </p>

<p align="center">

| **Componente** | **Preço** |
| :-------------: | :--------: |
| Braço mecânico - MG400 | R$ 32000,00 |
| Desenvolvedor Front-end | R$ 4.704,00 |
| Desenvolvedor Back-end | R$ 7.807,00 |
| Engenheiro da Computação | R$ 8.052,00 |
| Programador de Automação Industrial | R$ 5.800,00 |
| Product Owner (PO) | R$ 13.818,00 |
| Manutenção (mensal) | R$ 1600,00 |
| Raspeberry Pi Pico W | R$ 49,90 |
| Instalação do MG400 | R$ 1000,00 |
| Auxiliar De Farmácia Hospitalar | R$ 1.932 |

</p>

&emsp;Atualmente, o parceiro Hospital Sírio-Libanês enfrenta problemas de demora na montagem de kits de emergência, além de frequentes erros durante esse processo. Essas questões são decorrentes de um método manual, suscetível a falhas humanas.

&emsp;Foi identificado que o responsável pela montagem dos kits de emergência é o Auxiliar de Farmácia hospitalar, que desempenha outras atividades além dessa e custa ao hospital, em média, dois mil reais por mês. Com a automação utilizando um braço robótico, o auxiliar ainda será necessário, mas apenas para configurar a montagem do kit. Dessa forma, o auxiliar terá mais tempo para realizar outras tarefas que dependem de suas habilidades e experiência, direcionando suas atividades no hospital para aquelas em que a presença humana seja realmente essencial.

&emsp;Apesar do custo inicial de R$75.626,00 e um custo mensal posterior de R$2.100, compreendemos que essa não é uma solução economicamente vantajosa. No entanto, a utilização de um braço mecânico na montagem dos kits trará mais segurança hospitalar, reduzindo as chances de contaminação, e maior precisão durante o processo, resultando em escolhas de medicamentos mais acertadas pelos médicos em situações de emergência.


&emsp;É importante notar que os ganhos do projeto impactam diretamente que os benefícios do projeto repercutem diretamente em um atendimento mais eficiente aos pacientes, proporcionando maior satisfação. Esses ganhos também têm impacto nos processos legais que o hospital poderia enfrentar devido a erros médicos, conferindo uma maior segurança para evitar gastos imprevistos nesse sentido.

---

# Value Proposition Canvas

&emsp;O Value Proposition Canvas é uma ferramenta utilizada para garantir que haja compatibilidade entre o produto desenvolvido e o mercado. Ele consiste em dois componentes principais: o perfil do cliente, que descreve os segmentos de clientes, suas necessidades e tarefas, e a proposta de valor, que detalha os benefícios oferecidos e como atendem às necessidades dos clientes. Essa abordagem técnica corrobora para a criação de produtos e serviços mais alinhados com as expectativas do mercado-alvo. 

<p align="center"><b>Quadro 1 - DValue Proposition Canvas do Hospital Sírio Libanês</b> </p>

<center>![Nao encontrei a imagem](../../../static/img/value-proposition-canvas.png) </center>


<p align="center"><b>Fonte: Elaborado pelos próprios autores </b> </p>

&emsp;O componente da proposta de valor consiste em "Ganhos criados", "Produtos e serviços" e "Dores aliviadas". Os ganhos criados para o Sírio-Libanês com a automação incluem uma adaptação dinâmica e rápida, aumento da eficiência operacional e precisão na montagem do carrinho de medicamentos. Os produtos e serviços compreendem um sistema integrado com um braço robótico e uma interface que garante uma maior segurança na montagem. Isso contribui para a eficiência da logística e permite um controle preciso sobre os insumos em movimento, proporcionando acesso às mais recentes tecnologias, enquanto alivia as dores com a minimização de erros, rastreamento preciso e eficaz e automatização eficiente.

&emsp;O segmento do cliente compreende "Ganhos", "Tarefas do Cliente" e "Dores". Os "Ganhos" envolvem benefícios como eficiência na montagem, flexibilidade e agilidade, otimização da logística e rastreamento preciso dos insumos. A "Tarefa do Cliente" consiste em ser adaptável nas mudanças de layouts, fazer o monitoramento de itens e a montagem dos carrinhos. As "Dores" são representadas pela falta de rastreamento interno para os insumos, a ausência de flexibilidade e o tempo gasto na montagem manual dos kits e carrinhos de emergência.

---

## Bibliografia:

SOLAR, N. Preço da energia elétrica CPFL 2023. Disponível em: https://www.ngsolar.com.br/single-post/preco-kwh-cpfl#:~:text=Com%20o%20reajuste%20de%202023.

LTDA, I. B. A. DE I. Salário de Auxiliar De Farmácia Hospitalar | Infojobs. Disponível em: https://www.infojobs.com.br/salario/auxiliar-farmacia-hospitalar. Acesso em: 16 fev. 2024.

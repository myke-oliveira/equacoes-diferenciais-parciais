# Equações Diferenciais Parciais

Este repositório apresenta alguns *Jupyter Notebooks* para ilustrar equações diferencias parciais (EDPs) estudadas em uma disciplina introdutória de uma graduação em Matemática. Abaixo uma breve descrição de algumas EDPs.

## Equação de Laplace

Modela a transferência de calor em regime estacionário. A variável $ u(x, y, z) $ representa a temperatura em um ponto. Esta mesma equação também pode ser usada para representar o potêncial elétrico em uma região do espaço sem cargas elétricas.

$$
\nabla^2 u = 0
$$

## Equação de Poisson

Este é um caso mais geral da equação de Laplace, $ u(x, y, z) $ representa o potêncial elétrico em uma região e $ \rho $ representa a distribuição de cargas.

$$
\nabla^2 u = \rho
$$

## Equação de Calor

Esta equação representa a tranferência de calor em regime transiente. A variável $ u(x, y, z, t) $ representa a temperatura na posição $ (x, y, z) $ e no instante $ t $.

$$
\nabla^2 u = \alpha u_t
$$

## Equação da Onda

Esta equação representa uma onda que se propaga no espaço

$$
\nabla^2 u = \alpha u_{tt}
$$

# Projeto de Estudos

Durante as aulas, foi feito um projeto de estudos, [clique aqui](./artigo/main3.pdf) para acessar.

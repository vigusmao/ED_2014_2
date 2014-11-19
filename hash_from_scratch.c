#include<stdlib.h>
#include<strings.h>

#define TAMANHO 200

typedef struct _ALUNO {
    int dre;
    char nome[30];
    float cra;
} ALUNO;

typedef struct _ELEMENTO {
    int chave;
    ALUNO* objeto;
    struct _ELEMENTO* prox;
} ELEMENTO;

int h(int chave) {
    return chave % TAMANHO;
}

ALUNO* buscar(ELEMENTO** tabela, int chave) {
    printf("\nBuscando aluno com chave %d...", chave);

    ALUNO* resultado = NULL;
    int indice = h(chave);
    ELEMENTO* elemento = tabela[indice];

    int offset = 0;
    while (elemento != NULL) {
        if (elemento->chave == chave) {
            resultado = elemento->objeto;
            break;
        }
        elemento = elemento->prox;
        offset++;
    }

    if (resultado != NULL) {
        printf("\nAluno encontrado (%d/%d) -- nome: %s, CRA: %f",
               indice, offset, resultado->nome, resultado->cra);
    } else {
        printf("\nAluno nao encontrado!!!!");
    }

    return resultado;
}

void inserir(ELEMENTO** tabela, int chave, ALUNO* aluno) {
    printf("\nInserindo aluno com chave %d...", chave);

    if (buscar(tabela, chave) != NULL) {
        printf("\nO aluno de chave %d ja existe!", chave);
        return;
    }

    int indice = h(chave);
    ELEMENTO* elemento = (ELEMENTO*) malloc(sizeof(ELEMENTO));
    elemento->chave = chave;
    elemento->objeto = aluno;
    elemento->prox = tabela[indice];
    tabela[indice] = elemento;

    printf("\nElemento inserido no indice %d.", indice);
}

int main() {

    ELEMENTO** tabela = (ELEMENTO**) malloc(TAMANHO * sizeof(ELEMENTO*));

    ALUNO* novo_aluno;

    novo_aluno = (ALUNO*) malloc(sizeof(ALUNO));
    novo_aluno->dre = 1234;
    strcpy(novo_aluno->nome, "Vinicius");
    novo_aluno->cra = 6.5;

    inserir(tabela, novo_aluno->dre, novo_aluno);

    novo_aluno = (ALUNO*) malloc(sizeof(ALUNO));
    novo_aluno->dre = 434;
    strcpy(novo_aluno->nome, "Jose");
    novo_aluno->cra = 10;

    inserir(tabela, novo_aluno->dre, novo_aluno);

    buscar(tabela, 1234);
    buscar(tabela, 434);
    buscar(tabela, 111);
    buscar(tabela, 634);

    printf("\n\n");
    return 0;
}

#include<stdio.h>
#include<string.h>
#include<stdlib.h>


typedef struct _ELEMENTO {
   int DRE;
   char nome[30];
   float CRA;
   struct _ELEMENTO* prox;
} ELEMENTO;


typedef struct _LISTA_ENCADEADA {
   ELEMENTO* primeiro;
   ELEMENTO* ultimo;
   int cont;
} LISTA_ENCADEADA;


void inserir(LISTA_ENCADEADA* lista, ELEMENTO* novo, 
             ELEMENTO* antecessor) {
    if (antecessor == NULL) {
        novo->prox = lista->primeiro;
        lista->primeiro = novo;
    } else {
        novo->prox = antecessor->prox;
        antecessor->prox = novo;       
    }       
    
    if (antecessor == lista->ultimo) {
        lista->ultimo = novo;
    }
    lista->cont++;  
}

void print_lista(LISTA_ENCADEADA* lista) {
    ELEMENTO* no;
    no = lista->primeiro;
    while (no != NULL) {
        printf("\n%d - %s", no->DRE, no->nome);
        no = no->prox; 
    }
}


int main() {
    LISTA_ENCADEADA minha_lista;
    minha_lista.cont = 0;
    minha_lista.primeiro = NULL;
    minha_lista.ultimo = NULL;
    
    // Uma maneira de se fazer: instancie diretamente a struct e passe seu endereco
    
    ELEMENTO aluno1;
    aluno1.DRE = 111;
    aluno1.CRA = 8.5;
    strcpy(aluno1.nome, "Aluno1");
    inserir(&minha_lista, &aluno1, NULL);
    
    // Outra maneira: crie o ponteiro e aloque memória para ele, 
    // passando depois o proprio ponteiro
    
    ELEMENTO* aluno2_ptr;
    aluno2_ptr = (ELEMENTO*) malloc(sizeof(ELEMENTO));    
    aluno2_ptr->DRE = 222;
    aluno2_ptr->CRA = 6;
    strcpy(aluno2_ptr->nome, "Aluno2");
    inserir(&minha_lista, aluno2_ptr, &aluno1);    
    
    
    print_lista(&minha_lista);

    printf("\n");
    return 1;
}

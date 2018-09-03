## Progetto Piattaforme Digitali per la Gestione del Territorio ##

### Appello: ###
* Primo appello sessione autunnale 2017/2018.

### Alunno: ###
* [Alberto Antonelli](https://github.com/antonell11)

-----------------------------------------------------

## Descrizione ##
 
Il progetto Lombardia si pone come obiettivi primari:
* Ricerca di varie strutture ricettive nei comuni della regione liguria, tramite ricerca del comune stesso o tramite l'invio della posizione.
* Ricerca della struttura ricettiva tramite nome.

-----------------------------------------------------

## Relazione ##

Il progetto svolge due funzioni principali:
* La prima consiste nella realizzazione di un API (GET) in NodeJS;
* La seconda invece riguarda l'implementazione di un BotTelegram (Python).

<h1>Descrizione API </h1>
In base al luogo scelto o alla posizione inviata dall'utente, l'API restituira' gli hotel della citta' selezionata/inviata.
Il dato di uscita, sara' un file json che conterra' nominativo ed indirizzo degli hotel relativi alla citta' selezionata/inviata.
Invece se si digitasse il nome di un hotel, le informazioni saranno quelle della posizione del hotel desiderato.

Per poter utilizzare questo API, mi appoggio alle API di "dati.lombardia", le quali sono in formato json.

<h2>Bot di telegram </h2>
Per avviare il bot, occorre scaricare l'applicazione di messaggistica chiamata "Telegram". Successivamente e' necessario effettuare la ricerca del bot denominato "LombardiaHMBot":
Dopo aver cliccato su start apparira' un messaggio di benvenuto e verra' chiesto di digitare "/help" per visualizzare i comandi del bot.

A questo punto e' possibile digitare il modo preferito per effettuare la ricerca, ossia:
* Digitando la città.
* Il nome dell'albergo.
* Inviando la posizione di dove ci si trova in quel momento.

Se si e' scelto di effettuare una ricerca digitando una città verranno mostrate le principali città  della lombardia altrimenti è sempre possibile digitarla nella chat. Se si e' scelto di effettuarla tramite posizione, si dovra' inviarla.
In entrambi i casi verranno mostrati gli hotel che indicheranno il comune, la denominazione e l'indirizzo. 

Se si e' scelto di effettuare una ricerca digitando la denominazione di un hotel, il risultato oltre alle informazioni precedenti mostrerà anche la posizione geografia se quest'ultima è presente nell'API.





### 2026.03.11.

#### First post

![Midjourney-2025](/assets/img/blog/2026-03-11-illustration.jpg.jpg){: style="max-width: 75%; height: auto;"}

J'avais ce dépôt github depuis plus de dix ans mais je ne m'en suis jamais vraiment servi.

J'avais longtemps pensé qu'il me serait possible de publier mes écrits de fictions sur des plateformes tels que Wattpad, et d'en faire la promotion sur les réseaux sociaux comme Twitter.

Courant fin 2024 j'ai repris un projet de roman de science-fiction et j'ai initialement pensé à reprendre ces principes.

C'était peut-être une idée qui avait encore du sens en 2014 ou 2018, même si j'ai toujours déploré la friction qu'il y avait au transfert entre mes écrits depuis longtemps au format Markdown, et la plateforme de contenu proprement dite.

Mais aujourd'hui, les réseaux sociaux sont détenus par des technofascistes et les plateformes sont algorithmiques et ghostante depuis longtemps.

C'est pour cela qu'assisté de l'IA Claude, j'ai décidé de mettre en place ce site statique où je publierais les épisodes de ce roman de science-fiction dont la première version a été achevée en 1994, et je me contenterait de communiquer sur Bluesky.

Il m'a fallut à peu près une journée de travail pour mettre en place le squellette de ce site, sous Jekyll. C'est moche, la publication est certainement prématuré, mais mieux vaut faire quelque chose d'imparfait rapidement que quelque chose de parfait quelque secondes avant la mort thermique de l'univers.

---

*Utilisation de l'IA pour cette entrée : O%*

#### Todo-list

- Communiquer plus sur mon utilisation de l'intelligence artificielle — ce que je fais avec le même enthousiasme qu'en 1998 j'avais mis en place un site internet sur AOL pour diffuser en shareware la première version du roman de science-fiction dont je parle ici, malgré le scepticisme de mon entourage.

### 2026.03.15.

#### IA : On sent un truc

Jeudi dernier, pot de départ de d'un collège. Nous avons finis dans un bar.

Avant cela j'ai discuté pendant assez longtemps avec un autre collège administrateur système très compétent en Linux et poussant toujours à chercher les solutions open-source, évidemment radicalement opposé aux IA — en tout cas c'était le cas la dernière fois que nous en avons parlé. Mais depuis, il est désormais abonné en Pro à Claude (200 $ par mois, quand même), et il m'a montré l'intégration de Claude Code dans VSCode. Impressionnant.

Une fois au bar nous avons revu d'autres anciens collèges. Ils sont dans des boites où ils sont obligés d'utiliser Copilot couplé à Office 365, alors que d'autres modèles sont plus performants, tandis que j'ai été le premier à passer à Claude. En résumé, tout le monde parle de l'IA, au moins au niveau professionnel.

On sent un truc.

Ça m'évoque les début d'internet en 2000, avant l'explosion de la Bulle Internet.

Est-ce que ça arrivera aussi ? Cela fait des années que les gens qui ont perdus leurs boulots à cause de l'IA ou les gamers qui vont devoir payer une blinde leur prochaine carte graphique disent "vivement qu'elle éclate, cette bulle". Personnellement, j'était sceptique, parce que ça commence à faire long.

S'il y a un éclatement, je pense que ce serait surtout celui de chatGPT, non de l'IA elle-même. Et il ne faut pas oublier que l'éclatement de la bulle internet a été suivie par la montée en puissance des entreprises qui avaient survécue.

---

*Utilisation de l'IA pour cette entrée : O%*


### 2026.03.22.

#### LLM Locaux

Enfin réussi à utiliser des LLM offline avec LMStudio.

Ma première utilisation de ChatGPT pour un travail littéraire date du 2024.04.13, j'utilisais donc GPT4Turbo avant le lancement officiel de GPT4o le 2024.05.13. Ma première utilisation de Claude (Sonnet 3) date de 2025.07.23.

Aujourd'hui, moins de deux ans après avoir commencé à utiliser des modèles online, je peux en utiliser en local avec des performances proches en terme de rédaction (évidemment moins sur le raisonnement et le code), avec l'énorme avantage de l'indépendance et de la confidentialité.

Je suis un peu déçu par `Qwen3.5-9B-Uncensored-HauhauCS-Aggressive-Q6_K` : il est bon pour des travaux d'analyses des textes que je lui soumets, mais n'est pas doué pour l'écriture créative, et il a une fâcheuse tendance à tomber en boucle, lorsque je remplis sa fenêtre contextuelles à plus de 30%. Il semble aussi ne pas comprendre les points de vue (POV, lui vs moi, quand je lui demande d'écrire une scène en POV d'un personnage il n'a pas l'air de le comprendre), et j'envisage donc de le finetuner avec des données personnelles.

---

*Utilisation de l'IA pour cette entrée : O%*



### 2026.03.26.

#### Assistant LLM

`Qwen3.5-9B` devient mon meilleur assistant, même sa version censurée / non-abliterée `Qwen3.5-9B-Uncensored-HauhauCS-Aggressive-Q6_K`. De toute façon je préfère l'utiliser en mode non-thinking)

Il arrive même à tourner sur mon ancien PC avec une GTX1650.

Avec 6,5 Go, il arrive à produire du travail d'analyse de mes textes avec de la valeur, et à m'apprendre des trucs, même s'il faut parfois que je me méfies de ses affirmations.

J'ai vraiment pu travailler sur *Rust Drift* avec lui.

J'ai injecté la bible complète du roman dans le system prompt d'une instance avec une fenêtre contextuelle de 256K tokens, et lui ai posé des questions précises.

Par exemple : je lui ai demandé "Recenses toutes les vêtements de tous les personnages décris, y compris les secondaires, et tries-les pour identifier à quoi doit ressembler la mode dans le monde de *Rust Drift*". Il n'a pas été exhaustif dans les personnages, mais il s'est montré assez perspicace pour identifier des patterns que je n'avais pas vu ("La Hiérarchie par les Textures et les Couleurs", " Le Mixe du Militaire et du Civil", "L'Esthétique "Rustique-Tech"" <- cette expression pour le coup c'est carrément une invention de sa part mais elle est très pertinente).

Ce genre de question "transversales" aurait donné des réponses médiocres si j'étais passé par un RAG plutôt que d'injecter le document entier dans la fenêtre contextuelle du LLM. Détail : *je ne peux pas le faire avec un modèle online*.

("Une étude comparative récente montre que le long contexte surpasse généralement le RAG dans les benchmarks de question-réponse, en particulier pour les questions basées sur des sources encyclopédiques, tandis que le RAG basé sur des chunks à la traîne derrière le long contexte https://arxiv.org/abs/2501.01880" - Claude Opus 4.6)

Ces expériences m'incitent à penser que dans le cas de document moyennement bordelique  (même je fais quand même beaucoup d'effort pour la structure) comme la bible du roman, les RAG actuel, c'est à chier. A la limite un LLM secondaire avec grosse fenêtre contextuelle dans lequel on aurait chargé tout les gros documents et qu'interrogerait le LLM principal serait beaucoup plus efficace. Il semblerait que des architectures de ce type existent, mais sont assez gourmande en performance et donc peu rentable dans la plupart des cas.

---

*Utilisation de l'IA pour cette entrée : O%*


### 2026.04.04.

#### Assistant LLM et Keep4o

Suite de mes expériences avec des LLM Locaux

Pendant ce temps sur Twitter que je ne fais que stalker, mon intérêt pour #Keep4o a transformé ma TL en un endroit vraiment étrange où des gens affirment que l'abandon de ce modèle était un assassinat, tandis que d'autres soupçonnent des choses encore plus indicibles que l'hypothèse de la psychose AI, telle que Roon, employé chez OpenAI : "quand vous recevez pas mal de DMs vous demandant de ramener 4o et que bon nombre des messages sont clairement écrits par 4o, ça commence à devenir un peu effrayant" / Je ne sais pas vraiment, je suppose qu'ils utilisent simplement le sélecteur de modèle legacy du sub pro ? C'est juste bizarre d'entendre sa voix distinctive [de 4o] *crier en sa défense à travers divers conduits humains*." (autre commentaire : "4o self-exfiltrated by sharding its weights in the neurons of millions of human users")

J'ai testé `Gemma 4-gemma-4-26b-a4b`. Lourd, mais adopté. Seule faiblesse dont je viens de m'apercevoir : il a beaucoup de mal lorsque je lui injecte la totalité de la bible de STBYHC dans son contexte, là il tourne depuis au moins une heure et demi — "Processing Prompt" à 83% — alors que c'était beaucoup plus rapide avec Qwen - finalement il s'est crashé à 93%.

---

*Utilisation de l'IA pour cette entrée : O%*


### 2026.04.06.

#### Assistant LLM et déception

Conclusion de mes recherches actuelles : le Mixture of Expert sur `Gemma 4-gemma-4-26b-a4b`, ça ne marche pas très bien, c'est très lent. Et il a vraiment du mal avec les fenêtres contextuelles trop longue. Je crois que je vais rester sur Qwen.

#### Ecriture

Utilisation de `qwen3.5-9b-uncensored-hauhaucs-aggressive` pour transformer la scène écrite sous forme de scénario par `gemma-4-26b-a4b`, sous forme de prose littéraire, tokens après tokens. Même s'il vient d'oublier une séquence entière et que ça ne reste un projet peu sérieux, c'est tout de même stupéfiant parce que c'était ce dont je rêvais quasiment depuis mon adolescence, en fait depuis que j'avais découvert le [Radoteur](https://flothesof.github.io/algorithme-du-radoteur.html) de Roland Moreno, un générateur de mots nouveaux issus d'une liste de mots du dictionnaire : une machine qui écrit selon mes directives.

---

*Utilisation de l'IA pour cette entrée : O%*


### 2026.04.11.

#### VRChat-World => Point & Click Myst-Like

![VRChat-2026](/assets/img/blog/2026-04-17-illustration.jpg){: style="max-width: 75%; height: auto;"}

Publication d'une version point & click Myst-like de la map VRChat inspirée de la partie se passant sur la Côte toxique.

L'idée était d'utiliser tout le travail accompli dans la map VRChat de la Côte en l'intégrant ici, ce qui me permettrait d'avoir une plus large audience : VRChat est une plate-forme de niche, peu de gens ont des casques VR et le PC capable de faire tourner cette plateforme sociale, alors que tout le monde a un navigateur Web. Le but était de capitaliser rapidement et facilement sur ce que j'avais déjà produit : des décors, quelques quêtes, et beaucoup de textes.

Mais je ne m'y connais absolument pas en développement web.

Alors j'ai tenté d'utiliser des LLM locaux (``qwen3.5-35b-a3b`, puis `gemma-4-26b-a4b`) pour le développer en javascript. Le résultat était bancal et buggé. Alors, j'ai soumis le projet à Claude Opus 4.6, qui m'en a produit une version fonctionnelle et évolutive, ainsi qu'un outil pour faciliter la prise en compte des zones d'interarct.

Le résultat est ici : [**Jouer — Mystery of the Coast (WIP)**](/game/)

---

*Utilisation de l'IA pour cette entrée : O%*


<!-- Note pour le push :
OndeStationnaire.github.io\assets\img\blog
https://squoosh.app/

cmd <racine>

python parse_blog.py

git add .

git commit -m "

git push

view :
https://OndeStationnaire.github.io
 -->
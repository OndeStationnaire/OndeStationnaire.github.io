---
layout: post
date: 2026-03-26
title: "Assistant LLM"
---

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

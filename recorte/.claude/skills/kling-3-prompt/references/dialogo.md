# Diálogo e múltiplos personagens

O Kling 3.0 gera fala com voz por personagem, sotaque e code-switching entre idiomas, com lip sync e expressão facial coerentes com o timing da voz. O que quebra isso é ambiguidade sobre **quem** está falando e **quando**.

Quatro princípios.

## 1. Nome estruturado

Rótulos únicos e consistentes por personagem. Nunca pronome, nunca sinônimo.

✓ `[Character A: Black-suited Agent]`
✗ `[Agent] says… Then, he says…`

Se o personagem é "Marina" na primeira fala, ele é "Marina" em todas. Trocar pra "a mulher", "ela" ou "a executiva" faz o modelo tratar como pessoa nova.

## 2. Âncora visual

Amarre a fala a uma **ação física única** do personagem, e a ação vem antes da fala. Isso dá ao modelo o alvo de lip sync.

✓ Ação descrita, depois `[Nome do personagem, tom]: "Fala"`
✗ Fala solta sem ação âncora

## 3. Detalhe de áudio

Atribua tom e emoção únicos por personagem:

- `[Marina, raspy deep voice]`
- `[Leo, clear fearful voice]`

Marcadores de ritmo que funcionam: `fast urgent`, `shouting loudly`, `whispering`, `voice cracking`, `flat monotone`, `warm and slow`.

Vozes com descritores distintos separam melhor do que vozes descritas de forma parecida — se dois personagens têm tom similar, force o contraste (grave/aguda, rápida/lenta).

## 4. Controle temporal

Palavras de ligação controlam a sequência e evitam que as falas se fundam:

`Immediately,` · `Pause.` · `Then,` · `After a beat,`

Sem elas, o modelo tende a sobrepor as vozes.

## Template

```
[Cenário da cena com ambiência/música]

[Introdução do personagem com ação]
[Character A: Nome, tom]: "Fala"

Immediately, [ação do personagem B]
[Character B: Nome, tom]: "Fala"

[Ação continuada / direção de câmera]
[Nome do personagem, tom]: "Fala"
```

## Exemplo preenchido

```
Master Intent: A tense two-hander in a parked car at night. Rain on the
windshield, low engine hum, no music.

Scene 1 (Duration: 10s):
Medium two-shot from the back seat. Rain streaks the windows, dashboard
lights on their faces.

The driver grips the wheel with both hands and stares straight ahead.
[Character A: Driver, flat controlled voice]: "You said ten minutes."

Immediately, the passenger turns his head toward him, jaw tight.
[Character B: Passenger, fast urgent voice]: "I said ten minutes if it
went clean. It didn't go clean."

Pause. The driver slowly turns to face him.
[Character A: Driver, raspy low voice, almost whispering]: "Then get out."
```

## Fala em português

Escreva o corpo do prompt em inglês (a aderência a terminologia de câmera é melhor) e o **conteúdo da fala em português**, dentro das aspas. Os rótulos de tom permanecem em inglês.

```
The barista slides the cup across the counter and looks up.
[Character A: Barista, warm and slow voice]: "É a primeira vez que
você vem aqui, né?"
```

Se o vídeo é PT-BR e o sotaque importa, especifique: `[Character A: Barista, warm Brazilian Portuguese, São Paulo accent]`.

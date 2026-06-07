# mitx-6001-algorithms-python

**MITx 6.00.1x — Introduction to Computer Science and Programming in Python**

Algoritmos, estruturas de dados e análise de complexidade — base de engenharia antes de IA e infraestrutura.

---

## Benchmark — sorting

![Merge sort vs bubble sort — tempo vs n](docs/figures/sorting_benchmark.png)

| Algoritmo | Complexidade | Observação |
|-----------|--------------|------------|
| Merge sort | O(n log n) | Escala até n=8000 |
| Bubble sort | O(n²) | Limitado a n≤4000 (tempo) |

A divergência empírica confirma a análise assintótica do curso.

---

## Módulos

| Módulo | Tópico | Comando |
|--------|--------|---------|
| `sorting/` | Merge, bubble | `python sorting/run.py` |
| `scrabble/` | OOP — Scrabble | `python scrabble/ps4a.py` |
| `cipher/` | Cifra e ataque | `python cipher/ps6.py` |

## Setup

```bash
python docs/generate_figures.py
```

## Autor

**Guarantã Almeida** — [github.com/guaranta](https://github.com/guaranta)

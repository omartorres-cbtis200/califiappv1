# CalifiApp

Aplicación de consola en Python para **registrar y consultar las calificaciones de un grupo**.
Proyecto Scrum del Submódulo 2 · CBTIS 200 · 3AM PGR.

## Equipo Scrum
| Responsabilidad | Integrante |
|---|---|
| Product Owner | (OMAR) |
| Scrum Master | (AITOR) |
| Desarrolladores | (ALISON) |

## Requisitos
- Python 3.10 o superior
- Git

## Cómo ejecutar
```bash
git clone https://github.com/USUARIO/califiapp.git
cd califiapp
python src/main.py
```

## Cómo correr las pruebas
```bash
python -m unittest discover -s tests -v
```

## Ritual de cada clase (las computadoras del laboratorio se borran al reiniciar)
| Paso | Qué hago | Comando |
|---|---|---|
| 1 | Instalo Git | (instalador de git-scm.com) |
| 2 | Le digo a Git quién soy | `git config --global user.name "Mi Nombre"` y `git config --global user.email "micorreo@gmail.com"` |
| 3 | Traigo mi proyecto desde GitHub | `git clone https://github.com/USUARIO/califiapp.git` |
| 4 | Trabajo y pruebo | `python src/main.py` · `python -m unittest discover -s tests -v` |
| 5 | Guardo una foto del avance | `git add .` y `git commit -m "qué hice"` |
| 6 | Subo mi avance a la nube | `git push` |

> La computadora olvida todo al reiniciar. **GitHub no.**

## Estructura del proyecto
```
califiapp/
├── README.md          <- este archivo
├── .gitignore         <- lo que Git NO debe guardar
├── src/               <- código de la aplicación
│   ├── main.py            (menú de consola)
│   └── calificaciones.py  (lógica: una función por criterio)
├── tests/             <- pruebas automáticas
│   └── test_calificaciones.py
└── data/              <- archivos de datos (Sprint 2: JSON/CSV)
```

## Historias de usuario
| HU | Historia | Sprint |
|---|---|---|
| HU-01 | Registrar alumnos | 1 |
| HU-02 | Capturar calificaciones | 1 |
| HU-03 | Calcular promedio y estatus | 2 |
| HU-04 | Mostrar reporte del grupo | 3 |

Tablero del proyecto: (pega aquí la liga de tu GitHub Project)

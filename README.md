# Informe de Data Profiling de la Base de Datos NBA

## Descripción del Proyecto
Este análisis de datos forma parte de un proyecto de análisis de datos sobre la NBA, donde se analiza información detallada sobre los jugadores, los partidos y las estadísticas relacionadas con los tiros en los partidos de la liga.

## Data Profiling

**Columnas: 26**

1. SEASON_1
2. SEASON_2
3. TEAM_ID
4. TEAM_NAME
5. PLAYER_ID
6. PLAYER_NAME
7. POSITION_GROUP
8. POSITION
9. GAME_DATE
10. GAME_ID
11. HOME_TEAM
12. AWAY_TEAM
13. EVENT_TYPE
14. SHOT_MADE
15. ACTION_TYPE
16. SHOT_TYPE
17. BASIC_ZONE
18. ZONE_NAME
19. ZONE_ABB
20. ZONE_RANGE
21. LOC_X
22. LOC_Y
23. SHOT_DISTANCE
24. QUARTER
25. MINS_LEFT
26. SECS_LEFT

### Problemas Encontrados

- **Comentarios al principio del archivo CSV**: Al cargar el dataframe, se encontraron comentarios al principio del archivo que necesitaron ser limpiados.
  
- **Datos Nulos**:
  - **Position group**: 5883 valores nulos
  - **Position**: 5883 valores nulos

- **Duplicados**: Se encontraron 59 filas duplicadas en los datos.

- **Conteo de Jugadores**: Hay un total de 995 jugadores únicos.

- **Nombres sobrantes**: Encontramos 963 players name y 954 id's. Mediante una serie de solicitudes nos dimos cuenta de que hay id's con más de un nombre asignado:

  PLAYER_ID
203493     2
1628384    2
1628408    2
1630197    2
1630214    2
1630231    2
1630288    2
1630527    2
1631466    2
Name: PLAYER_NAME, dtype: int64
PLAYER_ID 203493 tiene los nombres: ['Reggie Bullock Jr.' 'Reggie Bullock']
PLAYER_ID 1628384 tiene los nombres: ['OG Anunoby' 'O.G. Anunoby']
PLAYER_ID 1628408 tiene los nombres: ['PJ Dozier' 'P.J. Dozier']
PLAYER_ID 1630197 tiene los nombres: ['Aleksej Pokusevski' 'Alekesej Pokusevski']
PLAYER_ID 1630214 tiene los nombres: ['Xavier Tillman' 'Xavier Tillman Sr.']
PLAYER_ID 1630231 tiene los nombres: ['KJ Martin' 'Kenyon Martin Jr.']
PLAYER_ID 1630288 tiene los nombres: ['Jeff Dowtin Jr.' 'Jeff Dowtin']
PLAYER_ID 1630527 tiene los nombres: ['Brandon Boston Jr.' 'Brandon Boston']
PLAYER_ID 1631466 tiene los nombres: ['Nate Williams' 'Jeenathan Williams']

### Análisis Descriptivo

#### Resumen Estadístico de las Columnas Clave

| **Columna**       | **Media** | **Desviación Estándar** | **Mínimo** | **Máximo** |
|-------------------|-----------|-------------------------|------------|------------|
| SEASON_1          | 2003.78   | 1.40                    | 2002       | 2024       |
| TEAM_ID           | 1610613009| 8.65                    | 1610613000 | 1610613029 |
| PLAYER_ID         | 1123357   | 685,569                 | 1,713      | 1,642,013  |
| GAME_ID           | 22,109,060| 140,230,805             | 21,900,000 | 22,301,230 |
| LOC_X             | 0.0639    | 7.444                   | -25        | 25         |
| LOC_Y             | 10.097    | 7.313                   | 0.05       | 89.45      |
| SHOT_DISTANCE     | 13.57     | 10.59                   | 0          | 89         |
| QUARTER           | 2.48      | 1.13                    | 1          | 7          |
| MINS_LEFT         | 5.37      | 3.45                    | 0          | 12         |
| SECS_LEFT         | 28.86     | 17.41                   | 0          | 59         |

#### Tipos de Datos

Los tipos de las columnas están correctamente identificados en su mayoría, pero algunos campos necesitan ajustes:

- **GAME_DATE** debe ser convertido a tipo **fecha** ya que actualmente se encuentra en formato de objeto.
  
### Valores Únicos

A continuación se presenta un resumen de la cantidad de valores únicos por cada columna clave:

| **Columna**       | **Valores Únicos** |
|-------------------|--------------------|
| SEASON_1          | 5                  |
| SEASON_2          | 5                  |
| TEAM_ID           | 30                 |
| TEAM_NAME         | 31                 |
| PLAYER_ID         | 954                |
| PLAYER_NAME       | 963                |
| POSITION_GROUP    | 3                  |
| POSITION          | 15                 |
| GAME_DATE         | 779                |
| GAME_ID           | 5825               |
| HOME_TEAM         | 30                 |
| AWAY_TEAM         | 30                 |
| EVENT_TYPE        | 2                  |
| SHOT_MADE         | 2                  |
| ACTION_TYPE       | 48                 |
| SHOT_TYPE         | 2                  |
| BASIC_ZONE        | 7                  |
| ZONE_NAME         | 6                  |
| ZONE_ABB          | 6                  |
| ZONE_RANGE        | 5                  |
| LOC_X             | 949                |
| LOC_Y             | 1540               |
| SHOT_DISTANCE     | 89                 |
| QUARTER           | 7                  |
| MINS_LEFT         | 13                 |
| SECS_LEFT         | 60                 |


Шлях, знайдений DFS: ['Dejvicka', 'Hradcanska', 'Malostranska', 'Staromestska', 'Mustek', 'Narodni trida', 'Lazarska', 'Jindrisska', 'Hlavni nadrazi', 'Muzeum', 'I.P. Pavlova', 'Vysehrad', 'Prazskeho povstani', 'Pankrac', 'Budejovicka', 'Kacerov', 'Roztyly', 'Chodov', 'Opatov', 'Haje']
Кількість станцій у шляху DFS: 20

Шлях, знайдений BFS: ['Dejvicka', 'Hradcanska', 'Malostranska', 'Staromestska', 'Mustek', 'Muzeum', 'I.P. Pavlova', 'Vysehrad', 'Prazskeho povstani', 'Pankrac', 'Budejovicka', 'Kacerov', 'Roztyly', 'Chodov', 'Opatov', 'Haje']
Кількість станцій у шляху BFS: 16

DFS досліджує якомога глибше вздовж кожної гілки перед тим, як повернутися назад. Це може призвести до обхідних маршрутів і, як наслідок, довших шляхів у графі, особливо якщо існують різні варіанти для продовження.

BFS досліджує всі вершини на поточному рівні перед переходом до наступного рівня, що гарантує знаходження найкоротшого шляху в графі з ненавантаженими ребрами.

Результати пошуку:
Шлях, знайдений DFS, містить 20 станцій і включає додаткові відхилення через станції 'Narodni trida', 'Lazarska', 'Jindrisska', та 'Hlavni nadrazi'.
Шлях, знайдений BFS, містить 16 станцій і є прямішим, без зайвих відхилень. Це підтверджує, що BFS знайшов найкоротший шлях.

Висновки:
BFS знаходить найкоротший шлях у ненавантаженому графі, що підтверджується результатами, де BFS знайшов коротший шлях у порівнянні з DFS. Тобто BFS є кращим вибором для пошуку найкоротшого шляху в транспортних мережах, де важлива мінімізація кількості станцій або часу в дорозі. DFS може бути корисним у випадках, коли потрібно дослідити всі можливі маршрути або у великих графах, де можна очікувати великі глибини без численних відгалужень.
Різниця в довжині шляхів також показує, як структура графу впливає на ефективність алгоритмів. У лінійних або майже лінійних графах BFS зазвичай перевершує DFS у знаходженні коротших маршрутів.
Таким чином, для задачі пошуку найкоротшого шляху в транспортних мережах, таких як метрополітен, BFS є більш підходящим алгоритмом через його здатність знаходити найкоротші шляхи.
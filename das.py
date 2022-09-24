class DasEvaluator:
    def __init__(self):
        self.__das_questions_evaluation = {}

        self.__add_evaluation_for_questions(range(0, 15), {
            "Vždy shoda": 5,
            "Téměř vždy shoda": 4,
            "Občas neshoda": 3,
            "Často neshoda": 2,
            "Téměř vždy neshoda": 1,
            "Vždy neshoda": 0
        })

        self.__add_evaluation_for_questions(range(15, 17), {
            "Pořád": 0,
            "Často": 1,
            "Spíše častěji": 2,
            "Občas": 3,
            "Zřídka": 4,
            "Nikdy": 5
        })

        self.__add_evaluation_for_questions(range(17, 19), {
            "Pořád": 5,
            "Často": 4,
            "Spíše častěji": 3,
            "Občas": 2,
            "Zřídka": 1,
            "Nikdy": 0
        })

        self.__add_evaluation_for_questions(range(19, 22), {
            "Pořád": 0,
            "Často": 1,
            "Spíše častěji": 2,
            "Občas": 3,
            "Zřídka": 4,
            "Nikdy": 5
        })

        self.__add_evaluation_for_questions(range(22, 24), {
            "Každý den": 4,
            "Téměř každý den": 3,
            "Příležitostně": 2,
            "Zřídka": 1,
            "Nikdy": 0
        })

        self.__add_evaluation_for_questions(range(24, 28), {
            "Nikdy": 0,
            "Méně než jednou za měsíc": 1,
            "Jednou nebo dvakrát za měsíc": 2,
            "Jednou nebo dvakrát týdně": 3,
            "Jednou denně": 4,
            "Častěji než jednou denně": 5
        })

        self.__add_evaluation_for_questions(range(28, 30), {
            "Ano": 0,
            "Ne": 1
        })

        self.__add_evaluation_for_questions(range(30, 31), {
            "Krajně nešťastné": 0,
            "Značně nešťastné": 1,
            "Trochu nešťastné": 2,
            "Šťastné": 4,
            "Veľmi šťastné": 5,
            "Nesmírně šťastné": 6,
            "Dokonalé": 6
        })

        self.__add_evaluation_for_questions(range(31, 32), {
            "Nesmírně si přeji, aby se náš vztah vydařil, a udělal(a) bych pro to cokoliv.": 5,
            "Velmi si přeji, aby se náš vztah vydařil, a udělám vše, co je v mých silách, aby tomu tak bylo.": 6,
            "Velmi si přeji, aby se náš vztah vydařil, a budu k tomu poctivě přispívat.": 7,
            "Byl(a) bych rád(a), kdyby se náš vztah vydařil, ale sám(a) pro to nemohu udělat víc, než dělám.": 8,
            "Byl(a) bych rád(a), kdyby se náš vztah vydařil, ale odmítám pro to dělat víc, než dělám nyní.": 9,
            "Náš vztah se nemůže vydařit a já pro něj nemohu nic udělat.": 0
        })

    def score(self, answers):
        das_score = 0
        for question_num, das_answer in enumerate(answers):
            das_score += self.__das_questions_evaluation[question_num][das_answer]

        return das_score

    def __add_evaluation_for_questions(self, question_nums, evaluation):
        for question_num in question_nums:
            self.__das_questions_evaluation[question_num] = evaluation

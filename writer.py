import pandas as pd


class SheetWriter:
    def __init__(self, stls_scale_factor):
        self.__columns = ['Email address', 'Sex', 'Interview', 'Longer relationship than 3 years',
                          'Intimacy', 'Passion', 'Commitment', 'DAS']
        self.__filename = 'Summary.xlsx'

        self.__stls_scale_factor = stls_scale_factor

    def write(self, results):
        df = pd.DataFrame(results, columns=self.__columns)

        writer = pd.ExcelWriter(self.__filename, engine='xlsxwriter')

        styled = df.style.apply(self.highlight_ok_rows, axis=1)
        styled.to_excel(writer)

        writer.save()

    def highlight_ok_rows(self, rows):
        # general questions
        has_long_enough_relationship = rows.loc['Longer relationship than 3 years']

        # dyadic adjustment scale
        das = rows.loc['DAS']

        # sternberg's triangular love scale
        intimacy = rows.loc['Intimacy']
        passion = rows.loc['Passion']
        commitment = rows.loc['Commitment']

        if has_long_enough_relationship == 'Ano' and self.is_above_das_avg(das) and self.is_above_stls_avg(intimacy, passion, commitment):
            color = 'green'
        else:
            color = 'red'

        return ['background-color: {}'.format(color) for _ in rows]

    def is_above_das_avg(self, das_score):
        das_avg_min = 114.8

        return das_score >= das_avg_min * self.__stls_scale_factor

    def is_above_stls_avg(self, intimacy_score, passion_score, commitment_score):
        intimacy_avg_min = 111 * self.__stls_scale_factor
        passion_avg_min = 98 * self.__stls_scale_factor
        commitment_avg_min = 108 * self.__stls_scale_factor

        return intimacy_score >= intimacy_avg_min and passion_score >= passion_avg_min and commitment_score >= commitment_avg_min

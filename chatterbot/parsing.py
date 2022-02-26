import calendar

# Variations of dates that the parser can capture
year_variations = ['ano', 'anos']
day_variations = ['dias', 'dia']
minute_variations = ['minuto', 'minutos']
hour_variations = ['horas', 'hora']
week_variations = ['semanas', 'semana']
month_variations = ['mês', 'meses']

# Variables used for RegEx Matching
day_names = 'segunda-feira|terça-feira|quarta-feira|quinta-feira|sexta-feira|sábado|domingo'
month_names_long = (
    'janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro'
)
month_names = month_names_long + '|jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez'
day_nearest_names = 'hoje|ontem|amanhã|esta noite'
numbers = (
    r'(^a(?=\s)|um|dois|três|quatro|cinco|seis|sete|oito|nove|dez|'
    r'onze|doze|treze|quatorze|quinze|dezesseis|dezessete|'
    r'dezoito|dezenove|vinte|trinta|quarenta|cinquenta|sessenta|setenta|'
    r'oitenta|noventa|cem|mil)'
)
re_dmy = '(' + '|'.join(day_variations + minute_variations + year_variations + week_variations + month_variations) + ')'
re_duration = r'(antes|depois|mais cedo|mais tarde|atrás|de\neve)'
re_year = r'(19|20)\d{2}|^(19|20)\d{2}'
re_timeframe = r'este|chegando|próximo|seguinte|anterior|último|fim\de\o'
re_ordinal = r'st|nd|rd|th|primeiro|segundo|terceiro|quarto|quinto|' + re_timeframe
re_time = r'(?P<hour>\d{1,2})(?=\s?(\:\d|(a|p)m))(\:(?P<minute>\d{1,2}))?(\s?(?P<convention>(am|pm)))?'
re_separator = r'of|at|on'

NUMBERS = {
    'zero': 0,
    'um': 1,
    'dois': 2,
    'três': 3,
    'quatro': 4,
    'cinco': 5,
    'seis': 6,
    'sete': 7,
    'oito': 8,
    'nove': 9,
    'dez': 10,
    'onze': 11,
    'doze': 12,
    'treze': 13,
    'quatorze': 14,
    'quinze': 15,
    'dezesseis': 16,
    'dezessete': 17,
    'dezoito': 18,
    'dezenove': 19,
    'vinte': 20,
    'trinta': 30,
    'quarenta': 40,
    'cinquenta': 50,
    'sessenta': 60,
    'setenta': 70,
    'oitenta': 80,
    'noventa': 90,
    'cem': 100,
    'mil': 1000,
    'milhão': 1000000,
    'bilhão': 1000000000,
    'trilhão': 1000000000000,
}


# Mapping of Month name and Value
HASHMONTHS = {
    'janeiro': 1,
    'jan': 1,
    'fevereiro': 2,
    'fev': 2,
    'março': 3,
    'mar': 3,
    'abril': 4,
    'abr': 4,
    'maio': 5,
    'mai': 5,
    'junho': 6,
    'jun': 6,
    'julho': 7,
    'jul': 7,
    'agosto': 8,
    'ago': 8,
    'setembro': 9,
    'set': 9,
    'outubro': 10,
    'out': 10,
    'novembro': 11,
    'nov': 11,
    'dezembro': 12,
    'dez': 12
}

# Days to number mapping
HASHWEEKDAYS = {
    'segunda-feira': 0,
    'seg': 0,
    'terça-feira': 1,
    'ter': 1,
    'quarta-feira': 2,
    'qua': 2,
    'quinta-feira': 3,
    'qui': 3,
    'sexta-feira': 4,
    'sex': 4,
    'sábado': 5,
    'sáb': 5,
    'Domingo': 6,
    'dom': 6
}

# Ordinal to number
HASHORDINALS = {
    'zero': 0,
    'primeiro': 1,
    'segundo': 2,
    'terceiro': 3,
    'quarto': 4,
    'quinto': 5,
    'sexto': 6,
    'sétimo': 7,
    'oitavo': 8,
    'nono': 9,
    'décimo': 10,
    'décimo primeiro': 11,
    'décimo segundo': 12,
    'décimo terceiro': 13,
    'décimo quarto': 14,
    'décimo quinto': 15,
    'décimo sexto': 16,
    'décimo sétimo': 17,
    'décimo oitavo': 18,
    'décimo nono': 19,
    'vigésimo': 20,
    'último': -1
}

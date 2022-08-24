from django.db.models import Count, Max


def task_1(accounts):
    '''Задача 1.
    Агрегационный запрос по каждому пользователю
    выводит последнее действие и общее количество
    для каждого из типов 'actions', из чего
    впоследствии формируется итоговый список'''
    # агрегационный запрос
    aggregation_query = (
        accounts.values('number', 'sessions__actions__type').
        annotate(count=Count('sessions__actions'),
                 last=Max('sessions__actions__created_at')).
        order_by('number')
    )
    final_list = []
    type_dict = {
        'r': 'read',
        'c': 'create',
        'u': 'update',
        'd': 'delete'
    }
    for dict in aggregation_query:
        if (
            len(final_list) == 0 or final_list[-1]['number'] != dict['number']
        ):
            new_acc_table = {
                'number': dict['number'],
                'actions': [
                    {
                        'type': 'read',
                        'last': None,
                        'count': 0
                    },
                    {
                        'type': 'create',
                        'last': None,
                        'count': 0
                    },
                    {
                        'type': 'update',
                        'last': None,
                        'count': 0
                    },
                    {
                        'type': 'delete',
                        'last': None,
                        'count': 0
                    }
                ]
            }
            final_list.append(new_acc_table)
        for action in final_list[-1]['actions']:
            if (action['type'] == type_dict[dict['sessions__actions__type']]):
                action['count'] = dict['count']
                action['last'] = dict['last']
                break
    print(aggregation_query)
    return final_list


def task_2(accruals, payments):
    '''Задача 2.
    Функция возвращает словарь pyment:accrual
    и список с неиспользованными payments'''
    table = {}
    payments_accrualless = []
    for payment in payments:
        suitable_accruals = accruals.filter(date__lte=payment.date)
        if not suitable_accruals.exists():
            payments_accrualless.append(payment)
        else:
            same_month_accruals = suitable_accruals.filter(month=payment.month)
            if same_month_accruals.exists():
                accrual = same_month_accruals.last()
            else:
                accrual = suitable_accruals.first()
            table[payment] = accrual
            accruals = accruals.exclude(id=accrual.id)
    return (table, payments_accrualless)

from django.http import JsonResponse
from django.shortcuts import HttpResponse

from .models import Account, Accrual, Payment
from .tasks import task_1, task_2


def task_1_view(request):
    accounts = Account.objects.all()
    final_list = task_1(accounts)
    response = JsonResponse(final_list, safe=False)
    return response


def task_2_view(request):
    accruals = Accrual.objects.order_by('date')
    payments = Payment.objects.order_by('date')
    table, payments_accrualless = task_2(accruals, payments)
    response = HttpResponse()
    response.write("<table><tr><th>Payments</th><th>Accruals</th></tr>")
    for payment in table.keys():
        accrual = table[payment]
        response.write(
            "<tr>" +
            f"<td>{payment.id} {payment.date}</td>" +
            f"<td>{accrual.id} {accrual.date}</td>" +
            "</tr>"
        )
    response.write("</table>")
    response.write("<p>Список платежей, которые не нашли себе долг:</p><ul>")
    for payment_accrualless in payments_accrualless:
        response.write(
            "<li>" +
            f"{payment_accrualless.id} {payment_accrualless.date}" +
            "</li>"
        )
    response.write("</ul>")
    return response

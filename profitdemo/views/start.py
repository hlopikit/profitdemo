from django.shortcuts import render
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth


@main_auth(on_start=True, set_cookie=True)
def start(request):

    user = request.bitrix_user
    but = request.bitrix_user_token
    deals = but.call_list_method('crm.deal.list')

    methods = [("d{}".format(d['ID']), 'crm.deal.productrows.get', {"ID": d['ID']}) for d in deals]
    productrows = but.batch_api_call(methods)


    for d in deals:
        d['items_count'] = len(productrows.successes["d{}".format(d['ID'])]['result'])



    return render(request, 'start_page.html', locals())

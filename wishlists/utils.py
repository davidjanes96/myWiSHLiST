from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateWishlists(request, wishlists, results):

    #pagination
    page = request.GET.get('page')
    paginator = Paginator(wishlists, results)

    try:
        wishlists = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        wishlists = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        wishlists = paginator.page(page)
    
    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, wishlists
from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size=2
    page_query_param='p'#to change default page to any other value http://127.0.0.1:8000/student/?page=2
    page_size_query_param='records' #when client want to configure how many records ,he want to see on per page
    #eg. http://127.0.0.1:8000/student/?p=1&records=5 on page 1 I want 5 records to be shown
    max_page_size=7 #used to set above comment that max 7 items could be attached and not above that
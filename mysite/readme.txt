Example

- If we type in name of website like home/start
- So urls.py in mysite will check if we have a path named home or not. If we have it remove the home/ part and send start to
  the file where we include it
   path('home/', include("main.urls"))
- As in the above example we included main.urls so it will go to urls.py in main and check if we have a path name start
  it will now take us to the view associated with it
  In this case it is views.index
   path("start", views.index, name="index")
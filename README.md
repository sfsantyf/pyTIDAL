# pyTIDAL
**WHAT IS?**

This .py script can be used for this functions based in TIDAL:

1. Obtain tracks from album.
2. Obtain albums from artists.

(MORE FEATURES ARE COMING... OR YOU CAN ADD FEATURES AND MAKE PULL REQUEST, I would really appreciate your contribution. :) )

**HOW TO PREPAIR?**

1. You should edit "main.py".
2. This API requires access to an account to be able to work with its functions, we will prepare this in the next step.
3. In the first lines you can see a couple of variables with the name of **"id"** and **"password"**, you must insert in "id" the email of your TIDAL account and in "password", the password of your TIDAL account. _(Sorry for this huge privacy failure, it is a matter of this API works, you can read the source https://github.com/tamland/python-tidal)_

**HOW TO USE?**

1. Download and execute the script with python3.
2. You can view a menu with options, you should write the number option, for example: 
~~~ 
>>> | 1. Obtain album tracks / 2. Obtain artist albums / 3. About... | 

** Write "1" for obtain tracks from any album **

>>1

>>>> Obtain album tracks...
~~~

3. Search any album in TIDAL, copy and paste the URL with only the ID, for example:
~~~
https://listen.tidal.com/album/ **35143655** <- You should use this ID and paste in the script execution
~~~

4. The album tracks are printed in the console ;)

~~~
- The Mother We Share
- We Sink
- Gun
- Tether
- Lies
- Under the Tide
- Recover
- Night Sky
- Science/Visions
- Lungs
- By the Throat
- You Caught the Light
- Strong Hand
- Broken Bones
- Gun (KDA Remix)
- The Mother We Share (We Were Promised Jetpacks Remix)
~~~


import tidalapi

#PUT YOUR USERNAME (EMAIL) AND TIDAL PASSWORD IN THE VARIABLES (ITS A TIDAL CONFIGURATION, SORRY ABOUT PRIVACY FAIL); YOU CAN READ TIDALAPI SOURCE IN https://github.com/tamland/python-tidal#
id = ''
password = ''


#LABELS FOR OPTIMIZE CODE#
tidalSession = tidalapi.Session()
tidalFavorites = tidalapi.Favorites(tidalSession, id)


#LOGIN#
tidalSession.login(id, password)
tidalSession.check_login()


#THIS FUNCTION OBTAINS ALBUM TRACKS FROM "userGetAlbumTracks" VARIABLE#
def tidalGetAlbumTracks():
    userGetAlbumTracks = int(input(">>"))
    tracks = tidalSession.get_album_tracks(album_id=userGetAlbumTracks)
    for track in tracks:
        print(f"- {track.name}")

#THIS FUNCTION OBTAINS ARTIST ALBUMS FROM "userGetArtistAlbums" VARIABLE#
def tidalGetArtistAlbums():
    userGetArtistAlbums = int(input(">>"))
    albums = tidalSession.get_artist_albums(artist_id=userGetArtistAlbums)
    for album in albums:
        print(f"- {album.name}")

#WHILE TRUE EXECUTION, A PRINCIPAL MENU FOR CHOOSE OPTIONS#
while True:
    tidalMenuOptions = ('>>>> | 1. Obtain album tracks / 2. Obtain artist albums / 3. About... |')
    print(tidalMenuOptions)
    tidalMenuOptions = int(input(">>"))

    #CHOOSE OPTIONS#
    if tidalMenuOptions==1:
        print(">>>> Obtain album tracks...")
        tidalGetAlbumTracks()

    elif tidalMenuOptions==2:
        print(">>>> Obtain artist albums...")
        tidalGetArtistAlbums()



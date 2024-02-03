package music;

public class TestMusicStore {
    public static void main(String[] args)
    {

        MusicStore musicStore = new MusicStore("MusicStore1","Warsaw");
        musicStore.addAlbum("Album1");
        musicStore.addAlbum("Album2");
        System.out.println(musicStore);
        musicStore.removeAlbum("Album1");
        System.out.println(musicStore);

        VinylStore vinylStore = new VinylStore("Vinyl1","Olsztyn",100);
        vinylStore.addAlbum("Album1");
        vinylStore.addAlbum("Album2");
        System.out.println(vinylStore);
        vinylStore.removeAlbum("Album1");
        System.out.println(vinylStore);


    }
}

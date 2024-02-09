package music;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class TestSong {
    public static void main(String[] args) {

        List<Song> songs = new ArrayList<>();
        songs.add(new Song("Song1", "Artist1", 200));
        songs.add(new Song("Song2", "Artist2", 300));
        songs.add(new Song("Song3", "Artist3", 500));
        songs.add(new Song("Song4", "Artist4", 200));
        songs.add(new Song("Song5", "Artist5", 100));

        Collections.sort(songs);

        for(int i = 0; i < songs.size();i++)
        {
            System.out.println(songs.get(i));
        }


    }
}

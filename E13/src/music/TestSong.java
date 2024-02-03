package music;

import java.util.Arrays;
import java.util.Comparator;

public class TestSong {
    public static void main(String[] args) {
        Song[] songs = {new Song("Title1","Artist1",100),
        new Song("Title2","Artist2",150),
        new Song("Title3","Artist3",200)};

        Arrays.sort(songs,new DurationComparator().thenComparing(new ArtistTitleComparator()));


        for(int i = 0; i < songs.length;i++)
        {
            System.out.println(songs[i]);
        }
    }

}

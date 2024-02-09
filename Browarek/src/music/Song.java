package music;

public record Song(String title, String artist, int duration) implements Comparable<Song>
{
    @Override
    public int compareTo(Song o) {
        int wynik = Integer.compare(this.duration,o.duration);
        if(wynik==0)
        {
            return o.title.compareTo(this.title);
        }
        return wynik;
    }
}


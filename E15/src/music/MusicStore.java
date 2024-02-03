package music;

import java.util.ArrayList;
import java.util.Objects;

public class MusicStore {
    private String name;
    private String city;
    private ArrayList<String> albums;


    public void addAlbum(String album)
    {
        albums.add(album);
    }
    public void removeAlbum(String album)
    {
        albums.remove(album);
    }
    public MusicStore(String name, String city) {
        this.name = name;
        this.city = city;
        this.albums = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public ArrayList<String> getAlbums() {
        return new ArrayList<>(albums);
    }

    public void setAlbums(ArrayList<String> albums) {
        this.albums = albums;
    }

    @Override
    public boolean equals(Object object) {
        if (this == object) return true;
        if (!(object instanceof MusicStore that)) return false;
        return Objects.equals(name, that.name) && Objects.equals(city, that.city) && Objects.equals(albums, that.albums);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, city, albums);
    }

    @Override
    public String toString() {
        return "MusicStore{" +
                "name='" + name + '\'' +
                ", city='" + city + '\'' +
                ", albums=" + albums +
                '}';
    }
}

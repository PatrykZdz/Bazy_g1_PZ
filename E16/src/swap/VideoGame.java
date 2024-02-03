package swap;

public class VideoGame {
    private String name;
    private String developer;
    private float rating;

    public VideoGame(String name, String developer, float rating) {
        this.name = name;
        this.developer = developer;
        this.rating = rating;
    }

    @Override
    public String toString() {
        return "VideoGame{" +
                "name='" + name + '\'' +
                ", developer='" + developer + '\'' +
                ", rating=" + rating +
                '}';
    }

    public static void main(String[] args) {

        VideoGame[]videoGames = {new VideoGame("Game1", "Developer1", 9.5f),
                new VideoGame("Game2", "Developer2", 8.0f),
                new VideoGame("Game3", "Developer3", 7.2f)};

        Swap.swapElements(videoGames,0,2);

        for(int i = 0; i< videoGames.length;i++)
        {
            System.out.println(videoGames[i]);
        }


    }
}

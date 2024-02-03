package sports;

public record Athlete(String name,String sport,int yeraOfAchivement) implements Comparable<Athlete>
{

    @Override
    public int compareTo(Athlete o) {
        return Integer.compare(this.yeraOfAchivement,o.yeraOfAchivement); /// Rosnaco
    }

}

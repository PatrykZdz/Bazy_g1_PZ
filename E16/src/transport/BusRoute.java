package transport;

public record BusRoute(String routeNumber, String startLocation, String endLocation)
{
    public BusRoute
    {
        if(routeNumber== null || routeNumber.isEmpty())
            throw new IllegalArgumentException();
    }

    public boolean isLongRoute()
    {
        if(routeNumber.length() > 4)
        {
            return true;
        }
        return false;
        /// return routeNumber.length() > 4; lepiej
    }
    public void printDetails()
    {
        System.out.println("RouteNumber: "+ routeNumber+ "StartLocation: "+ startLocation+
                "EndLocation: "+ endLocation);

    }

}

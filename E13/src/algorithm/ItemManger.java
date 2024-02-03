package algorithm;

import java.util.ArrayList;

public class ItemManger<T> {
    private ArrayList<T> lista;
    {
        lista = new ArrayList<>();
    }

    public void addItem(T item)
    {
        lista.add(item);
    }
    public T getItem(int index)
    {
        return lista.get(index);
    }
    public int getItemCount()
    {
        return lista.size();
    }


    @Override
    public String toString() {
        return "ItemManger{" +
                "lista=" + lista +
                '}';
    }
}


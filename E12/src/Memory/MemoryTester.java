package Memory;

public class MemoryTester {
    public static void main(String[] args) {
        RAMManager ramManager = new RAMManager();
        DiskManager diskManager = new DiskManager();

        ramManager.allocateMemory(1024);
        ramManager.freeMemory();

        diskManager.allocateMemory(2048);
        diskManager.freeMemory();

        String memory = MemoryManager.getMemoryType();
        System.out.println(memory);

    }


}

import java.util.ArrayList;
import java.util.Scanner;

public class TodoListApp {
    static class Task {
        String description;
        boolean completed;

        Task(String description) {
            this.description = description;
            this.completed = false;
        }
    }

    private static ArrayList<Task> tasks = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\nMenu:\n1. View Tasks\n2. Add Task\n3. Complete Task\n4. Exit");
            System.out.print("Choose an option (1-4): ");
            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    listTasks();
                    break;
                case "2":
                    System.out.print("Enter new task: ");
                    String taskDesc = scanner.nextLine();
                    addTask(taskDesc);
                    break;
                case "3":
                    listTasks();
                    System.out.print("Enter task number to complete: ");
                    try {
                        int taskNum = Integer.parseInt(scanner.nextLine());
                        completeTask(taskNum);
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid number.");
                    }
                    break;
                case "4":
                    System.out.println("Goodbye!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }

    private static void listTasks() {
        if (tasks.isEmpty()) {
            System.out.println("No tasks found.");
            return;
        }
        System.out.println("\nTo-Do List:");
        for (int i = 0; i < tasks.size(); i++) {
            Task t = tasks.get(i);
            System.out.printf("%d. [%s] %s\n", i + 1, t.completed ? "✓" : "✗", t.description);
        }
    }

    private static void addTask(String desc) {
        if (desc.trim().isEmpty()) {
            System.out.println("Task cannot be empty.");
            return;
        }
        tasks.add(new Task(desc));
        System.out.println("Task added.");
    }

    private static void completeTask(int num) {
        if (num > 0 && num <= tasks.size()) {
            tasks.get(num - 1).completed = true;
            System.out.println("Task marked as completed.");
        } else {
            System.out.println("Invalid task number.");
        }
    }
}

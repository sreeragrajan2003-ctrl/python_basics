foundation task completed
stretch task completed
challenege task completed
Employee is a base class storing name and salary, with a placeholder work() method.

Developer and Manager inherit from Employee and override work() with their own tasks.

Objects are created (Developer("Ravi", 50000), Manager("Priya", 70000)) and stored in a list.

A loop calls emp.work() for each object, demonstrating polymorphism — same call, different behavior.

self.name and self.salary store each employee’s data, and emp.__class__.__name__ shows their role.
from django.db import migrations


COURSES_DATA = [
    {
        "category": {"name": "Programming Languages", "icon": "💻"},
        "courses": [
            {
                "title": "Java Programming – Beginner to Pro",
                "description": "Master Java from the ground up. Learn OOP, collections, exception handling, multithreading, and build real-world console and GUI applications.",
                "level": "beginner",
                "language": "Hindi",
                "lessons": [
                    {"title": "Introduction to Java & JDK Setup", "content": "Install JDK & IntelliJ IDEA. Understand JVM, JRE, JDK difference. Write your first Hello World program.", "order": 1, "duration_minutes": 20, "is_free_preview": True},
                    {"title": "Data Types, Variables & Operators", "content": "Primitive types (int, float, char, boolean). Variable declaration and initialization. Arithmetic, relational, and logical operators.", "order": 2, "duration_minutes": 25},
                    {"title": "Control Flow – if, switch, loops", "content": "if-else, nested if. switch-case statements. for, while, do-while loops with break and continue.", "order": 3, "duration_minutes": 30},
                    {"title": "Object-Oriented Programming Basics", "content": "Classes and Objects. Constructors and this keyword. Encapsulation with getters/setters.", "order": 4, "duration_minutes": 35},
                    {"title": "Inheritance & Polymorphism", "content": "extends keyword and super(). Method overriding and overloading. Runtime polymorphism with upcasting.", "order": 5, "duration_minutes": 35},
                    {"title": "Exception Handling", "content": "try-catch-finally blocks. Checked vs unchecked exceptions. Custom exception classes.", "order": 6, "duration_minutes": 30},
                    {"title": "Collections Framework", "content": "ArrayList, LinkedList, HashMap, HashSet. Iterators and for-each loops. Choosing the right collection.", "order": 7, "duration_minutes": 40},
                    {"title": "File I/O & Streams", "content": "Reading and writing files with FileReader/FileWriter. Buffered streams for efficiency. Serialization basics.", "order": 8, "duration_minutes": 35},
                ],
                "quiz": {
                    "title": "Java Fundamentals Quiz",
                    "questions": [
                        {"text": "Which keyword is used to inherit a class in Java?", "option_a": "implements", "option_b": "extends", "option_c": "inherits", "option_d": "super", "correct_option": "B"},
                        {"text": "What is the size of int in Java?", "option_a": "2 bytes", "option_b": "4 bytes", "option_c": "8 bytes", "option_d": "Platform dependent", "correct_option": "B"},
                        {"text": "Which collection does NOT allow duplicate values?", "option_a": "ArrayList", "option_b": "LinkedList", "option_c": "HashSet", "option_d": "Vector", "correct_option": "C"},
                        {"text": "What does JVM stand for?", "option_a": "Java Virtual Machine", "option_b": "Java Visual Manager", "option_c": "Java Variable Method", "option_d": "Java Verified Module", "correct_option": "A"},
                        {"text": "Which block always executes in exception handling?", "option_a": "try", "option_b": "catch", "option_c": "finally", "option_d": "throw", "correct_option": "C"},
                    ]
                }
            },
            {
                "title": "Python Programming – Zero to Hero",
                "description": "Learn Python with a hands-on approach. Covers syntax, data structures, OOP, file handling, modules, and mini-projects like a calculator and to-do app.",
                "level": "beginner",
                "language": "Hindi",
                "lessons": [
                    {"title": "Python Setup & Your First Script", "content": "Install Python and VS Code. Running .py files and using the REPL. print(), variables, and comments.", "order": 1, "duration_minutes": 15, "is_free_preview": True},
                    {"title": "Data Types & Type Conversion", "content": "int, float, str, bool. type() and isinstance(). Implicit and explicit type conversion.", "order": 2, "duration_minutes": 20},
                    {"title": "Lists, Tuples, Sets & Dictionaries", "content": "Creating and modifying collections. Slicing, indexing, and common methods. When to use which collection.", "order": 3, "duration_minutes": 30},
                    {"title": "Functions & Lambda Expressions", "content": "Defining functions with def. *args and **kwargs. Lambda, map, filter, and reduce.", "order": 4, "duration_minutes": 30},
                    {"title": "Object-Oriented Python", "content": "Classes, objects, and __init__. Inheritance and method overriding. Magic/dunder methods (__str__, __len__).", "order": 5, "duration_minutes": 35},
                    {"title": "File Handling & Exception Handling", "content": "Opening, reading, writing files. with statement (context manager). try-except-finally blocks.", "order": 6, "duration_minutes": 25},
                    {"title": "Modules & Libraries", "content": "import and from-import. Standard library: os, sys, math, random. Installing packages with pip.", "order": 7, "duration_minutes": 20},
                    {"title": "Mini Project: To-Do CLI App", "content": "Build a command-line to-do list manager. Features: add, view, delete, mark complete. Save tasks to a JSON file.", "order": 8, "duration_minutes": 45},
                ],
                "quiz": {
                    "title": "Python Fundamentals Quiz",
                    "questions": [
                        {"text": "Which data structure is immutable in Python?", "option_a": "List", "option_b": "Dictionary", "option_c": "Tuple", "option_d": "Set", "correct_option": "C"},
                        {"text": "What is the output of type(3.14) in Python?", "option_a": "<class 'int'>", "option_b": "<class 'float'>", "option_c": "<class 'double'>", "option_d": "<class 'number'>", "correct_option": "B"},
                        {"text": "Which keyword defines a function in Python?", "option_a": "function", "option_b": "fun", "option_c": "define", "option_d": "def", "correct_option": "D"},
                        {"text": "How do you install a Python package?", "option_a": "python install pkg", "option_b": "pip install pkg", "option_c": "apt install pkg", "option_d": "npm install pkg", "correct_option": "B"},
                        {"text": "Which symbol is used for single-line comments in Python?", "option_a": "//", "option_b": "/* */", "option_c": "#", "option_d": "--", "correct_option": "C"},
                    ]
                }
            },
            {
                "title": "C Programming – Foundation of Computing",
                "description": "Build a rock-solid foundation with C. Learn memory management, pointers, arrays, structures, and file I/O — the building blocks of all modern languages.",
                "level": "beginner",
                "language": "Hindi",
                "lessons": [
                    {"title": "Introduction to C & Environment Setup", "content": "History of C and why learn it. Installing GCC and Code::Blocks. Structure of a C program: headers, main(), return 0.", "order": 1, "duration_minutes": 20, "is_free_preview": True},
                    {"title": "Variables, Data Types & I/O", "content": "int, float, char, double. printf() and scanf() functions. Format specifiers: %d, %f, %c, %s.", "order": 2, "duration_minutes": 25},
                    {"title": "Operators & Control Statements", "content": "Arithmetic, relational, logical, bitwise operators. if-else, switch. for, while, do-while loops.", "order": 3, "duration_minutes": 30},
                    {"title": "Functions & Recursion", "content": "Function declaration, definition, and call. Pass by value. Recursion with factorial and Fibonacci examples.", "order": 4, "duration_minutes": 30},
                    {"title": "Arrays & Strings", "content": "1D and 2D arrays. String functions: strlen, strcpy, strcat, strcmp. Character arrays vs string literals.", "order": 5, "duration_minutes": 35},
                    {"title": "Pointers – The Heart of C", "content": "Address and dereference operators (& and *). Pointer arithmetic. Pointers and arrays relationship.", "order": 6, "duration_minutes": 40},
                    {"title": "Structures & Unions", "content": "Defining and using struct. Nested structures. Union vs struct. typedef for clean code.", "order": 7, "duration_minutes": 30},
                    {"title": "File Handling in C", "content": "fopen, fclose, fread, fwrite, fprintf, fscanf. Modes: r, w, a, rb, wb. Error handling with errno.", "order": 8, "duration_minutes": 30},
                ],
                "quiz": {
                    "title": "C Programming Quiz",
                    "questions": [
                        {"text": "Which header file is required for printf() and scanf()?", "option_a": "stdlib.h", "option_b": "string.h", "option_c": "stdio.h", "option_d": "math.h", "correct_option": "C"},
                        {"text": "What does the & operator return when used with a variable?", "option_a": "Value of variable", "option_b": "Memory address of variable", "option_c": "Size of variable", "option_d": "Type of variable", "correct_option": "B"},
                        {"text": "Which function is used to compare two strings in C?", "option_a": "strcmp()", "option_b": "strcomp()", "option_c": "compare()", "option_d": "strcmp2()", "correct_option": "A"},
                        {"text": "What is the size of char in C?", "option_a": "2 bytes", "option_b": "4 bytes", "option_c": "1 byte", "option_d": "8 bytes", "correct_option": "C"},
                        {"text": "Which keyword is used to define a structure in C?", "option_a": "class", "option_b": "struct", "option_c": "object", "option_d": "record", "correct_option": "B"},
                    ]
                }
            },
            {
                "title": "C++ Programming – OOP & Beyond",
                "description": "Advance from C to C++. Master object-oriented programming, STL, templates, and modern C++11/14 features used in competitive programming and system development.",
                "level": "intermediate",
                "language": "Hindi",
                "lessons": [
                    {"title": "C++ Basics & Difference from C", "content": "cin and cout. References vs pointers. namespace std and using directive.", "order": 1, "duration_minutes": 20, "is_free_preview": True},
                    {"title": "Classes, Objects & Constructors", "content": "Defining classes with public/private. Default, parameterized, and copy constructors. Destructor and memory cleanup.", "order": 2, "duration_minutes": 30},
                    {"title": "Inheritance & Polymorphism", "content": "Single and multiple inheritance. Virtual functions and vtable. Pure virtual functions and abstract classes.", "order": 3, "duration_minutes": 35},
                    {"title": "Operator Overloading", "content": "Overloading +, -, ==, <<, >>. Friend functions. Overloading assignment and subscript operators.", "order": 4, "duration_minutes": 30},
                    {"title": "Templates & Generic Programming", "content": "Function templates and class templates. Template specialization. Using templates for type-safe containers.", "order": 5, "duration_minutes": 30},
                    {"title": "Standard Template Library (STL)", "content": "vector, map, set, queue, stack, priority_queue. Iterators and algorithms. sort(), find(), binary_search().", "order": 6, "duration_minutes": 40},
                    {"title": "Exception Handling in C++", "content": "try, catch, throw. Multiple catch blocks. Standard exceptions: std::runtime_error, std::out_of_range.", "order": 7, "duration_minutes": 25},
                    {"title": "Modern C++11 Features", "content": "auto keyword and range-based for loop. Lambda expressions. Smart pointers: unique_ptr, shared_ptr.", "order": 8, "duration_minutes": 35},
                ],
                "quiz": {
                    "title": "C++ OOP Quiz",
                    "questions": [
                        {"text": "Which concept allows a function to have the same name with different parameters?", "option_a": "Overriding", "option_b": "Overloading", "option_c": "Encapsulation", "option_d": "Abstraction", "correct_option": "B"},
                        {"text": "What is a virtual function used for?", "option_a": "Compile-time binding", "option_b": "Runtime polymorphism", "option_c": "Memory allocation", "option_d": "Template creation", "correct_option": "B"},
                        {"text": "Which STL container gives O(1) average access time by key?", "option_a": "vector", "option_b": "set", "option_c": "map (unordered_map)", "option_d": "list", "correct_option": "C"},
                        {"text": "What does the destructor do in C++?", "option_a": "Creates an object", "option_b": "Initializes values", "option_c": "Cleans up resources when object is destroyed", "option_d": "Copies an object", "correct_option": "C"},
                        {"text": "Which smart pointer gives exclusive ownership?", "option_a": "shared_ptr", "option_b": "weak_ptr", "option_c": "unique_ptr", "option_d": "auto_ptr", "correct_option": "C"},
                    ]
                }
            },
        ]
    },
    {
        "category": {"name": "Database Management", "icon": "🗄️"},
        "courses": [
            {
                "title": "DBMS – Database Management Systems",
                "description": "Understand relational databases from scratch. Learn ER diagrams, normalization, SQL queries, transactions, indexing, and real-world database design.",
                "level": "beginner",
                "language": "Hindi",
                "lessons": [
                    {"title": "Introduction to DBMS & Database Concepts", "content": "What is a database vs file system. DBMS architecture: 3-tier schema. DBMS vs RDBMS differences.", "order": 1, "duration_minutes": 25, "is_free_preview": True},
                    {"title": "ER Diagram – Entity Relationship Model", "content": "Entities, attributes, and relationships. Primary key, foreign key, composite key. Drawing ER diagrams for real problems.", "order": 2, "duration_minutes": 30},
                    {"title": "Relational Model & Keys", "content": "Tables, tuples, and attributes. Candidate key, primary key, super key, foreign key. Integrity constraints.", "order": 3, "duration_minutes": 30},
                    {"title": "SQL – DDL Commands", "content": "CREATE, ALTER, DROP, TRUNCATE. Defining constraints: NOT NULL, UNIQUE, CHECK, DEFAULT. Database and table creation.", "order": 4, "duration_minutes": 35},
                    {"title": "SQL – DML & Queries", "content": "INSERT, UPDATE, DELETE, SELECT. WHERE, ORDER BY, GROUP BY, HAVING. Aggregate functions: COUNT, SUM, AVG, MIN, MAX.", "order": 5, "duration_minutes": 40},
                    {"title": "SQL – Joins & Subqueries", "content": "INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN. Self-join and cross-join. Correlated vs non-correlated subqueries.", "order": 6, "duration_minutes": 40},
                    {"title": "Normalization – 1NF to BCNF", "content": "Functional dependencies and anomalies. 1NF, 2NF, 3NF step-by-step with examples. Boyce-Codd Normal Form.", "order": 7, "duration_minutes": 35},
                    {"title": "Transactions, ACID & Indexing", "content": "ACID properties explained. COMMIT, ROLLBACK, SAVEPOINT. B-Tree indexing and query optimization basics.", "order": 8, "duration_minutes": 35},
                ],
                "quiz": {
                    "title": "DBMS Concepts Quiz",
                    "questions": [
                        {"text": "What does ACID stand for in database transactions?", "option_a": "Atomicity, Consistency, Isolation, Durability", "option_b": "Access, Control, Integrity, Data", "option_c": "Atomicity, Concurrency, Integrity, Durability", "option_d": "Access, Consistency, Isolation, Dependency", "correct_option": "A"},
                        {"text": "Which SQL command removes all data but keeps the table structure?", "option_a": "DROP", "option_b": "DELETE", "option_c": "TRUNCATE", "option_d": "REMOVE", "correct_option": "C"},
                        {"text": "Which normal form eliminates partial dependencies?", "option_a": "1NF", "option_b": "2NF", "option_c": "3NF", "option_d": "BCNF", "correct_option": "B"},
                        {"text": "Which JOIN returns all rows from both tables including non-matching?", "option_a": "INNER JOIN", "option_b": "LEFT JOIN", "option_c": "RIGHT JOIN", "option_d": "FULL OUTER JOIN", "correct_option": "D"},
                        {"text": "What is a primary key?", "option_a": "Any column in a table", "option_b": "A column with NULL values", "option_c": "A column that uniquely identifies each row", "option_d": "A foreign key reference", "correct_option": "C"},
                    ]
                }
            },
        ]
    },
    {
        "category": {"name": "Web Development", "icon": "🌐"},
        "courses": [
            {
                "title": "Frontend Development – HTML, CSS & JavaScript",
                "description": "Build beautiful, responsive websites from scratch. Master HTML5, CSS3 (Flexbox & Grid), JavaScript ES6+, DOM manipulation, and deploy your first website.",
                "level": "beginner",
                "language": "Hindi",
                "lessons": [
                    {"title": "HTML5 – Structure of the Web", "content": "DOCTYPE, head, body, meta tags. Semantic elements: header, nav, main, section, footer. Forms, tables, and media elements.", "order": 1, "duration_minutes": 30, "is_free_preview": True},
                    {"title": "CSS3 – Styling & Selectors", "content": "Box model: margin, border, padding. Selectors: class, id, pseudo, attribute. Colors, fonts, and backgrounds.", "order": 2, "duration_minutes": 35},
                    {"title": "CSS Flexbox & Grid Layout", "content": "Flexbox: flex-direction, justify-content, align-items. CSS Grid: grid-template-columns, rows, areas. Building responsive layouts.", "order": 3, "duration_minutes": 40},
                    {"title": "Responsive Design & Media Queries", "content": "Mobile-first design approach. @media queries for breakpoints. Fluid images and flexible typography.", "order": 4, "duration_minutes": 30},
                    {"title": "JavaScript – Basics & DOM", "content": "Variables (let, const), data types, functions. DOM manipulation: querySelector, addEventListener. Event handling and form validation.", "order": 5, "duration_minutes": 40},
                    {"title": "JavaScript ES6+ Modern Features", "content": "Arrow functions, template literals. Destructuring and spread operator. Promises, async/await basics.", "order": 6, "duration_minutes": 35},
                    {"title": "CSS Animations & Transitions", "content": "transition property for smooth effects. @keyframes animations. Transform: rotate, scale, translate.", "order": 7, "duration_minutes": 25},
                    {"title": "Mini Project: Portfolio Website", "content": "Build a complete personal portfolio site. Sections: hero, about, projects, skills, contact form. Deploy to GitHub Pages.", "order": 8, "duration_minutes": 60},
                ],
                "quiz": {
                    "title": "Frontend Development Quiz",
                    "questions": [
                        {"text": "Which HTML tag is used to link an external CSS file?", "option_a": "<style>", "option_b": "<link>", "option_c": "<script>", "option_d": "<css>", "correct_option": "B"},
                        {"text": "Which CSS property controls the space INSIDE the element border?", "option_a": "margin", "option_b": "border", "option_c": "padding", "option_d": "spacing", "correct_option": "C"},
                        {"text": "Which JavaScript method selects an element by its CSS class?", "option_a": "getElementById()", "option_b": "getElementsByClass()", "option_c": "querySelector()", "option_d": "getElement()", "correct_option": "C"},
                        {"text": "Which CSS layout model uses rows and columns simultaneously?", "option_a": "Flexbox", "option_b": "Grid", "option_c": "Float", "option_d": "Position", "correct_option": "B"},
                        {"text": "What does 'async/await' help with in JavaScript?", "option_a": "Styling elements", "option_b": "Handling asynchronous operations cleanly", "option_c": "Creating HTML elements", "option_d": "Database queries", "correct_option": "B"},
                    ]
                }
            },
            {
                "title": "Backend Development – Django & REST APIs",
                "description": "Build production-ready backends with Django. Learn MVC architecture, ORM, authentication, REST APIs with DRF, and deploy to the cloud.",
                "level": "intermediate",
                "language": "Hindi",
                "lessons": [
                    {"title": "Backend Fundamentals & Django Setup", "content": "What is backend development. Install Django, create project and app. Understanding MVT (Model-View-Template) architecture.", "order": 1, "duration_minutes": 25, "is_free_preview": True},
                    {"title": "Django Models & ORM", "content": "Defining models with fields. Running migrations. ORM queries: filter, get, create, update, delete. Related objects and ForeignKey.", "order": 2, "duration_minutes": 35},
                    {"title": "Views, URLs & Templates", "content": "Function-based views (FBV). URL routing with urlpatterns. Template rendering, context, and template tags/filters.", "order": 3, "duration_minutes": 35},
                    {"title": "Django Forms & Validation", "content": "ModelForm and custom forms. Form validation and error display. Handling POST data securely (CSRF).", "order": 4, "duration_minutes": 30},
                    {"title": "Authentication & Authorization", "content": "Built-in auth: login, logout, register. @login_required decorator. User groups and permissions.", "order": 5, "duration_minutes": 30},
                    {"title": "Django REST Framework – Building APIs", "content": "Installing DRF and serializers. APIView and ViewSets. Browsable API and testing with Postman.", "order": 6, "duration_minutes": 40},
                    {"title": "JWT Authentication & API Security", "content": "Token-based authentication with simplejwt. Protecting API endpoints. CORS configuration.", "order": 7, "duration_minutes": 30},
                    {"title": "Deployment to Production", "content": "Using PostgreSQL instead of SQLite. Configuring gunicorn and nginx. Deploying to Railway or Render.", "order": 8, "duration_minutes": 45},
                ],
                "quiz": {
                    "title": "Backend Development Quiz",
                    "questions": [
                        {"text": "What does ORM stand for?", "option_a": "Object Relational Mapping", "option_b": "Object Runtime Model", "option_c": "Open Resource Manager", "option_d": "Operational Relational Method", "correct_option": "A"},
                        {"text": "Which Django command creates database tables from models?", "option_a": "python manage.py runserver", "option_b": "python manage.py migrate", "option_c": "python manage.py createtables", "option_d": "python manage.py syncdb", "correct_option": "B"},
                        {"text": "What HTTP status code means 'Not Found'?", "option_a": "200", "option_b": "401", "option_c": "500", "option_d": "404", "correct_option": "D"},
                        {"text": "What is CSRF protection used for?", "option_a": "Encrypting passwords", "option_b": "Preventing unauthorized form submissions", "option_c": "Speed optimization", "option_d": "Image compression", "correct_option": "B"},
                        {"text": "Which DRF component converts model data to JSON?", "option_a": "ViewSet", "option_b": "Router", "option_c": "Serializer", "option_d": "Permission", "correct_option": "C"},
                    ]
                }
            },
        ]
    },
    {
        "category": {"name": "Cloud Computing", "icon": "☁️"},
        "courses": [
            {
                "title": "Cloud Computing – AWS & DevOps Fundamentals",
                "description": "Understand cloud computing concepts and hands-on AWS services. Learn EC2, S3, RDS, Lambda, IAM, and basic DevOps: Docker, CI/CD pipelines.",
                "level": "intermediate",
                "language": "Hindi",
                "lessons": [
                    {"title": "Cloud Computing Fundamentals", "content": "What is cloud computing? IaaS, PaaS, SaaS explained. Public, private, hybrid cloud. Why companies move to cloud.", "order": 1, "duration_minutes": 25, "is_free_preview": True},
                    {"title": "AWS Core Services – EC2 & S3", "content": "Launching EC2 instances (virtual servers). Security groups and key pairs. S3 buckets: upload, access control, static hosting.", "order": 2, "duration_minutes": 35},
                    {"title": "AWS IAM – Identity & Access Management", "content": "Users, groups, roles, and policies. Principle of least privilege. Creating IAM roles for services.", "order": 3, "duration_minutes": 30},
                    {"title": "AWS RDS – Managed Databases", "content": "Setting up MySQL/PostgreSQL on RDS. VPC and subnet configuration. Backups and multi-AZ deployment.", "order": 4, "duration_minutes": 30},
                    {"title": "AWS Lambda – Serverless Computing", "content": "What is serverless? Creating Lambda functions. Triggers: API Gateway, S3, EventBridge. Pricing model.", "order": 5, "duration_minutes": 35},
                    {"title": "Docker – Containerization", "content": "Why containers over VMs. Writing Dockerfile. docker build, run, push. Docker Compose for multi-service apps.", "order": 6, "duration_minutes": 40},
                    {"title": "CI/CD with GitHub Actions", "content": "Understanding CI/CD pipeline. Writing GitHub Actions workflows (.yml). Auto-deploy to AWS on push.", "order": 7, "duration_minutes": 35},
                    {"title": "Cloud Security & Cost Optimization", "content": "AWS security best practices. AWS Cost Explorer and budgets. Auto-scaling and load balancing basics.", "order": 8, "duration_minutes": 30},
                ],
                "quiz": {
                    "title": "Cloud Computing Quiz",
                    "questions": [
                        {"text": "What does IaaS stand for?", "option_a": "Internet as a Service", "option_b": "Infrastructure as a Service", "option_c": "Integration as a Service", "option_d": "Information as a Service", "correct_option": "B"},
                        {"text": "Which AWS service is used for object storage?", "option_a": "EC2", "option_b": "RDS", "option_c": "S3", "option_d": "Lambda", "correct_option": "C"},
                        {"text": "What is the purpose of Docker?", "option_a": "Cloud database management", "option_b": "Package and run apps in containers", "option_c": "Monitor server performance", "option_d": "Manage DNS records", "correct_option": "B"},
                        {"text": "What does IAM control in AWS?", "option_a": "Network routing", "option_b": "Storage limits", "option_c": "User access and permissions", "option_d": "Server memory", "correct_option": "C"},
                        {"text": "AWS Lambda is an example of which computing model?", "option_a": "IaaS", "option_b": "PaaS", "option_c": "Serverless / FaaS", "option_d": "Virtual Machine", "correct_option": "C"},
                    ]
                }
            },
        ]
    },
    {
        "category": {"name": "AI & Machine Learning", "icon": "🤖"},
        "courses": [
            {
                "title": "AI & Machine Learning – Practical Guide",
                "description": "Dive into Machine Learning and AI with Python. Learn supervised/unsupervised learning, neural networks, scikit-learn, and build real projects like spam detection and image classification.",
                "level": "intermediate",
                "language": "Hindi",
                "lessons": [
                    {"title": "Introduction to AI & ML", "content": "AI vs ML vs Deep Learning hierarchy. Supervised, unsupervised, reinforcement learning. Real-world ML applications and career paths.", "order": 1, "duration_minutes": 25, "is_free_preview": True},
                    {"title": "Python for ML – NumPy & Pandas", "content": "NumPy arrays and operations. Pandas DataFrames: read, filter, group. Data cleaning: handling missing values and duplicates.", "order": 2, "duration_minutes": 35},
                    {"title": "Data Visualization – Matplotlib & Seaborn", "content": "Line, bar, scatter, histogram plots. Seaborn heatmaps and pair plots. Visualizing distributions and correlations.", "order": 3, "duration_minutes": 30},
                    {"title": "Supervised Learning – Regression", "content": "Linear Regression theory and implementation. Polynomial regression. Metrics: MSE, RMSE, R² score. Scikit-learn pipeline.", "order": 4, "duration_minutes": 35},
                    {"title": "Supervised Learning – Classification", "content": "Logistic Regression, Decision Trees, Random Forest. Train-test split and cross-validation. Confusion matrix, precision, recall, F1.", "order": 5, "duration_minutes": 40},
                    {"title": "Unsupervised Learning – Clustering", "content": "K-Means clustering algorithm. Elbow method to find optimal k. DBSCAN and hierarchical clustering basics.", "order": 6, "duration_minutes": 35},
                    {"title": "Neural Networks & Deep Learning Intro", "content": "Perceptron and multilayer networks. Activation functions: ReLU, Sigmoid, Softmax. Introduction to TensorFlow/Keras.", "order": 7, "duration_minutes": 45},
                    {"title": "Mini Project: Spam Email Classifier", "content": "Build a spam detector using NLP and ML. TF-IDF vectorization. Train Naive Bayes and evaluate on real dataset.", "order": 8, "duration_minutes": 60},
                ],
                "quiz": {
                    "title": "AI & Machine Learning Quiz",
                    "questions": [
                        {"text": "Which type of learning uses labeled data?", "option_a": "Unsupervised Learning", "option_b": "Reinforcement Learning", "option_c": "Supervised Learning", "option_d": "Transfer Learning", "correct_option": "C"},
                        {"text": "What does overfitting mean in ML?", "option_a": "Model performs well on both train and test data", "option_b": "Model performs too well on training data but poorly on new data", "option_c": "Model is too simple to learn patterns", "option_d": "Model has too few parameters", "correct_option": "B"},
                        {"text": "Which algorithm is used for clustering?", "option_a": "Linear Regression", "option_b": "Logistic Regression", "option_c": "K-Means", "option_d": "Decision Tree", "correct_option": "C"},
                        {"text": "What is the purpose of train-test split?", "option_a": "Speed up training", "option_b": "Reduce dataset size", "option_c": "Evaluate model on unseen data", "option_d": "Normalize features", "correct_option": "C"},
                        {"text": "Which Python library is most used for Machine Learning?", "option_a": "NumPy", "option_b": "Matplotlib", "option_c": "scikit-learn", "option_d": "Pandas", "correct_option": "C"},
                    ]
                }
            },
        ]
    },
]


def seed_courses(apps, schema_editor):
    Category = apps.get_model('courses', 'Category')
    Course = apps.get_model('courses', 'Course')
    Lesson = apps.get_model('courses', 'Lesson')
    Quiz = apps.get_model('courses', 'Quiz')
    Question = apps.get_model('courses', 'Question')

    for group in COURSES_DATA:
        cat_data = group["category"]
        category, _ = Category.objects.get_or_create(
            name=cat_data["name"],
            defaults={"icon": cat_data["icon"], "description": ""}
        )

        for course_data in group["courses"]:
            course, created = Course.objects.get_or_create(
                title=course_data["title"],
                defaults={
                    "description": course_data["description"],
                    "category": category,
                    "level": course_data["level"],
                    "language": course_data["language"],
                    "is_offline_available": True,
                }
            )
            if not created:
                continue

            for lesson_data in course_data["lessons"]:
                Lesson.objects.create(
                    course=course,
                    title=lesson_data["title"],
                    content=lesson_data["content"],
                    order=lesson_data["order"],
                    duration_minutes=lesson_data["duration_minutes"],
                    is_free_preview=lesson_data.get("is_free_preview", False),
                )

            quiz_data = course_data.get("quiz")
            if quiz_data:
                quiz = Quiz.objects.create(
                    course=course,
                    title=quiz_data["title"],
                    description=f"Test your knowledge of {course_data['title']}",
                )
                for q in quiz_data["questions"]:
                    Question.objects.create(
                        quiz=quiz,
                        text=q["text"],
                        option_a=q["option_a"],
                        option_b=q["option_b"],
                        option_c=q["option_c"],
                        option_d=q["option_d"],
                        correct_option=q["correct_option"],
                    )


def unseed_courses(apps, schema_editor):
    Category = apps.get_model('courses', 'Category')
    seeded_names = [
        "Programming Languages", "Database Management",
        "Web Development", "Cloud Computing", "AI & Machine Learning"
    ]
    Category.objects.filter(name__in=seeded_names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_courses, unseed_courses),
    ]

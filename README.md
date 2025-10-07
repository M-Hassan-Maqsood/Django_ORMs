# Django_ORMs

---
# School Management System

## Overview
This project is a **School Management System** built with **Django** and **Django REST Framework**.
It demonstrates:
- School, Teacher, Student, Course, and ExamResult relationships.
- API endpoints using **Generic API Views**.
- Practical **ORM Queries** (Aggregations, Subqueries, Case/When, Window Functions).
- **Lazy Evaluation** of Django Querysets.

---

## Models
- **School** -> Has many Teachers & Students.
- **Teacher** -> Belongs to a School, teaches many Courses.
- **Student** -> Belongs to a School, can enroll in multiple Courses.
- **Course** -> Taught by a Teacher, many-to-many with Students.
- **ExamResult** -> Student’s marks in a Course.

---

# Django Custom Serialization Demo

This project demonstrates a complete implementation of **custom serialization and deserialization** in Django REST Framework (DRF) without using `ModelSerializer`.  
It provides a clear understanding of how Django handles data conversion between **Python objects** and **JSON**, along with custom validations and manual create/update methods.

---

## Features

- Custom Serializer implementation without `ModelSerializer`
- Manual handling of:
  - Serialization (Model -> JSON)
  - Deserialization (JSON -> Python object)
  - Field-level validation
  - Object-level validation
  - Implements `create()` and `update()` methods
---


# 🐍 Aprendiendo Python

¡Bienvenido a mi repositorio para aprender Python desde cero! Aquí encontrarás apuntes, ejemplos y guías que te ayudarán a entender los fundamentos de este poderoso lenguaje de programación.

---

## 📖 Breve Historia de Python

Python fue creado por **Guido van Rossum** y lanzado por primera vez en 1991. Su nombre se inspiró en el grupo de comedia británico *Monty Python*. El objetivo principal de Python es ser un lenguaje simple, legible y potente.

> “Python es poderoso... y divertido.” – Guido van Rossum

---

## 👨‍🔬 Creador

- **Nombre:** Guido van Rossum  
- **Nacionalidad:** Neerlandés 🇳🇱  
- **Año de creación:** 1989 (prototipo), 1991 (versión pública)  
- **Motivación:** Crear un lenguaje fácil de aprender y de usar para todos

---

## 💾 Instalación de Python

Puedes instalar Python siguiendo estos pasos:

### 🔸 Windows / macOS / Linux:

1. Ve a la página oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Descarga la versión más reciente.
3. Instala marcando la opción ✅ `Add Python to PATH` durante el proceso.

### 🔍 Verifica instalación:

```bash
python --version
```
o

```bash
python3 --version
```

---

## 💼 Variables y Nomenclatura

A continuación, una tabla con tipos de variables y sus recomendaciones de nombre:

| Tipo de Dato   | Ejemplo de Variable | Convención de Nomenclatura |
|----------------|---------------------|-----------------------------|
| Entero         | `edad`              | minúsculas, palabras separadas por guiones bajos |
| Decimal        | `altura_metros`     | snake_case                  |
| Cadena         | `nombre_usuario`    | snake_case                  |
| Booleano       | `es_estudiante`     | prefijo booleano (`es_`, `tiene_`, `puede_`) |
| Lista          | `nombres_lista`     | plural si representa grupo  |
| Diccionario    | `datos_usuario`     | nombre descriptivo          |

---

## 🧪 Creación y Ejecución de un Entorno Virtual en Python

Usar un entorno virtual te permite mantener tus dependencias aisladas. Aquí te muestro cómo:

### 🛠️ Crear el entorno virtual

```bash
python -m venv venv
```

Esto creará una carpeta llamada `venv` con el entorno virtual.

### 🚀 Activar el entorno virtual

- **Windows:**

```bash
venv\Scripts\activate
```

- **macOS / Linux:**

```bash
source venv/bin/activate
```

### ❌ Desactivar el entorno virtual

```bash
deactivate
```

---

## 📦 Instalación de paquetes

Una vez activado el entorno, puedes instalar paquetes como:

```bash
pip install nombre_del_paquete
```

Para guardar las dependencias:

```bash
pip freeze > requirements.txt
```

Y para restaurarlas en otra máquina:

```bash
pip install -r requirements.txt
```

---

## 📚 Licencia

Este proyecto está bajo la licencia MIT. ¡Siéntete libre de usarlo y contribuir!

---

## ✍️ Autor

**Jeshit Lopes**  
📫 Contacto: [TuCorreo@example.com]  
🐙 GitHub: [github.com/TuUsuario](https://github.com/TuUsuario)

---

> *“La simplicidad es la máxima sofisticación” – Leonardo da Vinci*
# Propuesta de desarrollo web

## Proyecto
**Web oficial de autor en Django**

## 1. Resumen ejecutivo

Se propone el desarrollo de una web oficial para autor con una arquitectura modular, escalable y mantenible basada en Django.

El objetivo es contar con una plataforma profesional que permita:

- Publicar y gestionar libros.
- Mantener un blog con comentarios moderados.
- Editar contenidos institucionales sin tocar código.
- Gestionar contacto con envío de correos vía SMTP.
- Mantener identidad visual editorial, minimalista y responsive.

---

## 2. Objetivos del proyecto

### Objetivo general
Construir un sitio web profesional para presencia digital oficial del autor, con gestión completa desde panel administrador.

### Objetivos específicos

1. Implementar un catálogo de libros con fichas individuales.
2. Crear sección de blog con flujo de publicación y moderación de comentarios.
3. Habilitar sección “Sobre mí” editable por administración.
4. Permitir contacto mediante formulario (sin exponer email públicamente).
5. Garantizar base técnica preparada para crecimiento y despliegue en producción.

---

## 3. Alcance funcional

### 3.1 Sitio público

#### Inicio
- Frase destacada editable desde admin.
- Módulo de “Novedad” con el libro marcado como destacado.

#### Libros
- Listado visual del catálogo.
- Página de detalle por libro con portada, sinopsis, precio y enlace de compra.

#### Sobre mí
- Biografía editable.
- Fotografía del autor.

#### Blog
- Listado de artículos publicados.
- Detalle de artículo.
- Comentarios públicos solo tras aprobación manual.

#### Contacto
- Formulario de contacto con envío SMTP al correo del autor.
- Sin exposición pública del email.

### 3.2 Panel de administración

Gestión de:
- Perfil del autor (`AuthorProfile`).
- Libros (`Book`).
- Artículos (`Post`).
- Comentarios (`Comment`) con moderación manual.

Funcionalidades administrativas:
- Filtros y búsqueda.
- Slugs automáticos.
- Acciones masivas (publicar/despublicar, aprobar comentarios).

---

## 4. Enfoque técnico

### Backend
- Framework: Django.
- ORM: Django ORM.
- Base de datos: SQLite (fase inicial).

### Frontend
- HTML + CSS propio (sin frameworks UI).
- Diseño editorial minimalista, responsive y accesible.

### Seguridad/configuración
- Variables sensibles por `.env`.
- Configuración separada por entorno (`local` y `production`).
- Ajustes de producción con HTTPS y cabeceras seguras.

### SEO y calidad
- Metadatos base y OpenGraph.
- `robots.txt` y `sitemap.xml`.
- Plantillas de error 404/500.
- Tests base para páginas públicas y moderación.

---

## 5. Arquitectura propuesta

Estructura por dominios:

- `apps/core`: home, about, contacto, perfil de autor.
- `apps/books`: catálogo y detalle de libros.
- `apps/blog`: publicaciones y comentarios.
- `templates/`: layout base y parciales reutilizables.
- `static/css/`: estilos divididos por capas (`base`, `layout`, `components`, `pages`).

Esta arquitectura permite escalar funcionalidades futuras sin degradar mantenibilidad.

---

## 6. Plan de trabajo por fases

### Fase 1 · Base técnica
- Estructura de proyecto.
- Configuración de entornos.
- Modelado inicial y migraciones.

### Fase 2 · Módulos de contenido
- Inicio, Libros, Sobre mí.
- Panel admin completo para carga de contenido.

### Fase 3 · Blog y moderación
- Publicación de artículos.
- Comentarios con flujo de aprobación.

### Fase 4 · Contacto y SEO
- Formulario con SMTP.
- Metadatos, sitemap, robots y páginas de error.

### Fase 5 · QA y preparación de despliegue
- Pruebas funcionales base.
- Ajustes de seguridad y checklist de producción.

---

## 7. Entregables

1. Código fuente del proyecto Django.
2. Panel admin listo para operación de contenidos.
3. Documentación técnica del proyecto.
4. Documento de propuesta de desarrollo (este documento).
5. Checklist de puesta en producción.

---

## 8. Riesgos y mitigación

1. **Contenido inicial incompleto**
   - Mitigación: comando de bootstrap para poblar demo.

2. **Credenciales SMTP mal configuradas**
   - Mitigación: documentación y validación en entorno local.

3. **Spam en comentarios**
   - Mitigación: moderación manual + honeypot + limitación básica.

4. **Escalabilidad futura**
   - Mitigación: arquitectura modular por apps y separación de responsabilidades.

---

## 9. Recomendaciones de evolución

- Migrar a PostgreSQL en producción.
- Añadir analítica (GA4/Plausible).
- Implementar cache para listados.
- Añadir panel de métricas editoriales.
- Incorporar pipeline CI/CD con tests automáticos.

---

## 10. Cierre

La propuesta planteada garantiza una base sólida para una web oficial de autor profesional, operable por administración y preparada para crecimiento.

El proyecto se estructura con criterios de calidad técnica y editorial, priorizando mantenibilidad, seguridad y experiencia de usuario.

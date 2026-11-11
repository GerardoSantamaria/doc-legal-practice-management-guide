# Foja - Documentación del proyecto

Foja es un asistente para abogados del fuero laboral de la Provincia de Buenos Aires: guía cada expediente por su flujo procesal y calcula y avisa los vencimientos. El nombre es provisorio hasta verificar la marca (ver `identidad_y_diseno_v1.md`).

Este repositorio es **solo documental**: contiene la definición funcional, técnica y legal de la app. El código de la app vive en otros repositorios. Las herramientas de `herramientas/` sirven para mantener estos documentos, no forman parte del producto.

## Por dónde empezar

1. `analisis_y_definiciones_pendientes_v1.md`: registro de decisiones, arquitectura, seguridad y lo que falta definir. Es el documento que ordena a los demás.
2. `documentacion_de_proyecto_asistente_legal_pba.md`: concepto del producto, la matriz de flujo procesal y sus validaciones.
3. `backlog_historias_v1.md`: historias de la V1 con criterios de aceptación.

## Índice

| Documento | Contenido |
| :--- | :--- |
| `analisis_y_definiciones_pendientes_v1.md` | Decisiones, alcance de la V1, arquitectura, hosting, recuperación, seguridad, checklist. |
| `documentacion_de_proyecto_asistente_legal_pba.md` | Producto, matriz del flujo laboral de PBA (Ley 11.653), dudas para el abogado. |
| `logica_matematica_calculadora_de_dias_habiles_judiciales.md` | Reglas del motor de plazos, pseudocódigo y casos de prueba. |
| `modelo_de_base_de_datos_relacional.md` | Modelo de datos de PostgreSQL. |
| `definicion_de_ui_ux_asistente_legal.md` | Pantallas, navegación y comportamientos. |
| `identidad_y_diseno_v1.md` | Nombre, logo, paleta, tipografía, íconos, componentes base y tono de voz. Archivos en `diseno/`. |
| `diseno_de_pantallas_v1.md` | Todas las pantallas con captura: rutas, roles, contenido, acciones, estados y operaciones de la API. Maquetas HTML en `diseno/pantallas/`. |
| `modelado_de_amenazas_v1.md` | Activos, STRIDE por componente, controles, brechas y mapeo OWASP. |
| `api/openapi_v1.yaml` | Contrato de la API de la V1 (OpenAPI 3.1). |
| `backlog_historias_v1.md` | Épicas e historias de usuario de la V1. |
| `tareas_backend_v1.md` | Tareas técnicas del backend, de 1 a 3 días cada una, con dependencias. |
| `legal/` | Borradores de términos y condiciones, política de privacidad y acuerdo de encargo del tratamiento. Requieren revisión de un abogado antes de publicarse. |
| `matriz_flujo_laboral_pba_ley_11653.xlsx` | Matriz de ejemplo del flujo laboral, para validar con el abogado. |
| `diagrama_flujo_laboral_pba_ley_11653.md` | Diagramas Mermaid generados desde la matriz. |
| `herramientas/` | Scripts para regenerar la matriz, los diagramas y las tablas del documento de proyecto. Ver `herramientas/README.md`. |

# Dudas y puntos a validar · Proceso sucesorio PBA

**Estado:** borrador para validar · **Fecha:** 13/11/2026 · **Versión de la matriz:** 1 (borrador)

Este documento reúne lo que el abogado tiene que validar en [`matriz_flujo_sucesorio_pba.xlsx`](matriz_flujo_sucesorio_pba.xlsx): las 45 dudas de la hoja `Dudas_a_validar`, ordenadas por bloque, y las citas que quedaron marcadas "(a verificar)" en los hitos. El texto de cada duda es el mismo que el de la planilla.

---

## 1. Cómo se trabaja

- **La planilla es la fuente.** Cada respuesta se escribe en `Respuesta_Equipo_Legal`, con la norma o la acordada que la sostiene, y `Estado` pasa a `VALIDADO` o `CORREGIR`. Si la respuesta cambia un hito, se corrige también la fila en `Nodos` o en `Transiciones`, con su `Estado_Validacion`.
- **Además de las dudas, cada fila se valida.** Hay 61 hitos y 139 transiciones con `Estado_Validacion = PENDIENTE`. El control "filas pendientes" de la hoja `Flujo` las cuenta.
- **Ante la duda, el vencimiento más temprano.** Es el principio del motor: cada duda trae una propuesta por defecto que cumple ese principio. Una propuesta por defecto no se da por buena hasta que el abogado la acepte por escrito.
- **No correr `generar.py` sobre la planilla una vez que el abogado empiece a completarla:** la pisa con lo que hay en `datos/datos_sucesorio.py` (ver [`README.md`](README.md)).

## 2. Las cinco de mayor impacto

| Duda | Tema | Por qué primero |
| :--- | :--- | :--- |
| D05 y D06 | Edictos: cuántas publicaciones y Día Cero | Definen el vencimiento de la citación, que es el camino principal hacia la declaratoria. |
| D44 | Catálogos de la app | Sin un régimen civil, el fuero Civil y Comercial y los tipos de juzgado, este flujo no se puede importar. |
| D42 y D41 | Roles en un proceso sin demandado | Si representamos a un coheredero que impugna, los avisos de "te toca a vos" quedan invertidos. |
| D30 y D28 | ITGB y tasa de justicia | Sin estos pagos no se ordena la inscripción; el ITGB vence a los 15 días del pedido o a los 24 meses del fallecimiento. |
| D03 | Juzgados de Paz Letrados | Define en qué juzgado se inicia y si el trámite es el mismo. |

## 3. Bloque A · Régimen, competencia y fuentes

Definen qué normas y qué juzgados cubre el flujo.

### D01 · Régimen procesal y vigencia

¿Sigue vigente al 13/11/2026 el CPCCBA (Decreto-Ley 7425/68) sin reformas posteriores que toquen los arts. 724 a 773? La última reforma encontrada es la Ley 15.513 (BO 03/01/2025), que no toca el sucesorio; los textos de leyes-ar.com usados están actualizados al 16/10/2026. La noticia de noviembre de 2026 sobre un nuevo código procesal civil es de Santa Fe, no de PBA. Propuesta: la matriz se arma sobre el Decreto-Ley 7425/68. Fuentes: normas.gba.gob.ar (Leyes 11.511 y 15.513) y leyes-ar.com.

**Hitos afectados:** Todos

### D02 · Citas normativas

Validar artículo por artículo las citas del CPCCBA, del CCyC, del Código Fiscal y de las Leyes 7205, 6716, 14.967 y 13.951. Las marcadas '(a verificar)' no se pudieron confirmar en una fuente oficial o actualizada.

**Hitos afectados:** Todos

### D03 · Juzgados de Paz Letrados

Según el art. 61 de la Ley 5827 (texto Ley 13.645), los Juzgados de Paz Letrados conocen en sucesiones (ap. II inc. l), salvo los de los 20 partidos del ap. I (Almirante Brown, Avellaneda, Lanús, Tigre, Vicente López y otros). ¿Hay opción por el Juzgado Civil y Comercial cuando el peticionante no domicilia en el partido (art. 3 inc. 6 Ley 9229, citado por la Cámara de Trenque Lauquen el 28/04/2022)? ¿El trámite es el mismo? Propuesta: un solo flujo para los dos órganos; el tribunal elegido define el régimen. Fuente: normas.gba.gob.ar (Ley 5827).

**Hitos afectados:** SUC_030 (Último domicilio del causante y juzgado competente), SUC_100 (Escrito de inicio del sucesorio), SUC_112 (Radicación ante el juez competente)

### D04 · Mediación previa

La Ley 13.951 (art. 4 inc. 8) excluye de la mediación los 'juicios sucesorios y voluntarios' (verificado en normas.gba.gob.ar). ¿Las acciones contenciosas conexas (nulidad de testamento, petición de herencia, colación, reducción, partición contenciosa) necesitan mediación previa? Propuesta: el checklist de esos hitos avisa que hay que verificarlo.

**Hitos afectados:** SUC_650 (Colación y reducción para proteger la legítima), SUC_850 (Acción de nulidad o impugnación del testamento), SUC_860 (Impugnación de la declaratoria o petición de herencia)

## 4. Bloque B · Plazos y cómputo

Cada respuesta cambia un valor, un tipo de plazo o la gracia de un hito, y con eso la fecha de vencimiento.

### D06 · Edictos: cómputo

El art. 734 CPCCBA dice 'treinta (30) días corridos' y el art. 2340 CCyC 'treinta días' (art. 6 CCyC: días continuos, sin excluir inhábiles). ¿El Día Cero es la última publicación o el día siguiente, en que la resolución se tiene por notificada (art. 147 CPCCBA)? ¿La feria suspende el plazo? Propuesta (la más temprana): corridos, Día Cero en la última publicación y sin descontar la feria.

**Hitos afectados:** SUC_200 (Publicación de edictos y plazo de citación de herederos y acreedores)

### D07 · Citación de herederos instituidos

El art. 742 CPCCBA da 30 días para que se presenten los herederos instituidos, los beneficiarios y el albacea, sin decir si son corridos o hábiles. Si son varios, ¿corre desde la última notificación? Propuesta (la más temprana): corridos, desde la última notificación personal.

**Hitos afectados:** SUC_220 (Citación de herederos instituidos, beneficiarios y albacea)

### D12 · Registro de Juicios Universales

La Ley 7205 manda comunicar el inicio en 3 días (art. 3) y al Registro, informar en 10 días (art. 4). ¿Esos 10 días son hábiles judiciales? ¿Se diligencia hoy en forma electrónica? Propuesta: hábiles judiciales, sin gracia (es un plazo del Registro). Fuente: normas.gba.gob.ar (Ley 7205).

**Hitos afectados:** SUC_120 (Informe del Registro de Juicios Universales)

### D16 · Intimación a aceptar o renunciar

El art. 2289 CCyC deja al juez fijar entre 1 y 3 meses. La matriz propone 1 mes (el más temprano). ¿Se computa de fecha a fecha desde la notificación? ¿Admite gracia?

**Hitos afectados:** SUC_230 (Intimación a un heredero a aceptar o renunciar la herencia)

### D17 · Caducidad del derecho de opción

El art. 2288 CCyC fija 10 años desde la apertura de la sucesión (la muerte). Propuesta: sin gracia (es un plazo de fondo) y con límite a las 24:00 del día del vencimiento, la misma pregunta que la duda D28 de la matriz laboral hace para la prescripción. ¿Es correcto?

**Hitos afectados:** SUC_015 (Control de la caducidad del derecho de aceptar la herencia)

### D19 · Rendición de cuentas

Art. 748 CPCCBA y art. 2355 CCyC: trimestral; las parciales quedan 5 días en secretaría y la final 10. ¿Esos plazos son hábiles judiciales y corren desde la notificación? ¿El trimestre se cuenta desde la aceptación del cargo o por trimestre calendario?

**Hitos afectados:** SUC_420 (Rendición de cuentas del administrador)

### D21 · Inventario intimado

El art. 2341 CCyC da 3 meses desde la intimación judicial de acreedores o legatarios, y el art. 2321 inc. a hace responder al heredero con sus bienes si no cumple. ¿Sin gracia y con límite a las 24:00? ¿El Día Cero es la notificación de la intimación?

**Hitos afectados:** SUC_505 (Inventario intimado por acreedores o legatarios)

### D30 · ITGB: plazos

El art. 322 inc. b del Código Fiscal da 15 días desde la solicitud judicial de inscripción, entrega o libramiento de fondos, o 24 meses desde el fallecimiento, lo que ocurra primero (texto en leyes-ar.com, actualizado al 16/10/2026). ¿Los 15 días son corridos o hábiles administrativos? ¿Qué escrito cuenta como 'solicitud judicial de inscripción'? Propuesta (la más temprana): corridos, desde el escrito que pide la inscripción. La Ley 14.044 incorporó el impuesto al Código Fiscal desde el 01/01/2010.

**Hitos afectados:** SUC_016 (Vencimiento máximo del ITGB: 24 meses desde el fallecimiento), SUC_700 (Pedido de la orden de inscripción), SUC_910 (Declaración jurada y pago del ITGB ante ARBA)

### D31 · Honorarios y aportes

Art. 57 Ley 14.967: apelación en 5 días, fundada en el mismo acto. ¿Son hábiles judiciales desde la notificación por cédula y admiten gracia? Art. 14 Ley 6716: aportes dentro de 60 días corridos de firme la regulación. ¿Cuándo se pide la regulación en la práctica (al pedir la inscripción o por etapas)?

**Hitos afectados:** SUC_920 (Regulación de honorarios), SUC_925 (Apelación de la regulación de honorarios), SUC_930 (Pago de honorarios y depósito de los aportes de la Ley 6716)

### D36 · Caducidad de instancia

El sucesorio no caduca, salvo que se suscite controversia (art. 313 inc. 2 CPCCBA). ¿Qué plazo rige en los incidentes: 6 meses (art. 310 inc. 1, primera instancia) o 3 meses? La matriz propone 3, el más temprano. El art. 311 descuenta las ferias y el tipo MESES del motor no lo hace, así que el aviso queda antes del vencimiento real.

**Hitos afectados:** SUC_870 (Control de la caducidad de instancia en un incidente con controversia), SUC_875 (Intimación a activar el incidente bajo apercibimiento de caducidad)

### D37 · Ferias judiciales

La SCBA fija por acordada la feria de enero y dos semanas en invierno. Propuesta: los plazos en días hábiles judiciales se congelan; los corridos y los de meses y años no se suspenden (art. 6 CCyC); la caducidad sí descuenta las ferias (art. 311). ¿Es correcto para cada hito? Las reglas R1 a R9 del motor se validan en las dudas D26 a D34 de la matriz laboral y valen también para este flujo.

**Hitos afectados:** Todos

### D38 · Plazo de gracia

La matriz aplica la gracia del art. 124 CPCCBA solo a las presentaciones de parte en plazos procesales en días hábiles judiciales; no a los plazos de fondo del CCyC, del fisco (ITGB, aportes) ni de los organismos. ¿Es correcto?

**Hitos afectados:** SUC_015 (Control de la caducidad del derecho de aceptar la herencia), SUC_016 (Vencimiento máximo del ITGB: 24 meses desde el fallecimiento), SUC_200 (Publicación de edictos y plazo de citación de herederos y acreedores), SUC_220 (Citación de herederos instituidos, beneficiarios y albacea), SUC_230 (Intimación a un heredero a aceptar o renunciar la herencia), SUC_420 (Rendición de cuentas del administrador), SUC_505 (Inventario intimado por acreedores o legatarios), SUC_910 (Declaración jurada y pago del ITGB ante ARBA), SUC_930 (Pago de honorarios y depósito de los aportes de la Ley 6716)

### D39 · Notificaciones electrónicas

Según el reglamento de la SCBA (Acuerdo 4013, texto ordenado por el Acuerdo 4039, art. 13), la notificación electrónica se perfecciona el martes o viernes siguiente a quedar disponible; la compilación de la SCBA al 02/11/2026 lo mantiene vigente. ¿Qué notificaciones del sucesorio siguen siendo por cédula en papel (herederos denunciados sin domicilio electrónico, citación de instituidos)? Fuente: digesto.scba.gov.ar y scba.gob.ar.

**Hitos afectados:** SUC_200 (Publicación de edictos y plazo de citación de herederos y acreedores), SUC_220 (Citación de herederos instituidos, beneficiarios y albacea), SUC_530 (Traslado del inventario y avalúo o de la denuncia de bienes), SUC_620 (Traslado de la cuenta particionaria)

### D40 · Reposición y apelación

Confirmar que en el sucesorio rigen la reposición en 3 días (art. 239 CPCCBA), la apelación en 5 (art. 244), el memorial en 5 (art. 246) y la queja en 5 (art. 275), todos en días hábiles judiciales y con gracia.

**Hitos afectados:** SUC_800 (Reposición contra una providencia simple), SUC_810 (Apelación de una resolución del sucesorio), SUC_815 (Memorial de la apelación en relación)

## 5. Bloque C · Trámite hito por hito

Cambian checklists, documentación o caminos. Se pueden corregir en la planilla hasta la firma sin tocar código.

### D05 · Edictos: publicaciones y medio

El CCyC (art. 2340) manda un edicto por un día en el diario de publicaciones oficiales; el CPCCBA (art. 734 inc. 2) manda tres días en el Boletín Judicial y en otro diario del último domicilio, o solo en el Boletín Judicial si el haber prima facie no supera 900 Jus. ¿Qué se ordena hoy en cada departamento: lo del CCyC, lo del CPCCBA o una combinación? ¿El diario de publicaciones oficiales es el Boletín Oficial de PBA o el Boletín Judicial? La matriz no depende de la respuesta: el Día Cero es la última publicación, sea cual sea su número. Fuentes: leyes-ar.com (art. 734) y blogs.scba.gov.ar.

**Hitos afectados:** SUC_100 (Escrito de inicio del sucesorio), SUC_110 (Providencia de apertura del sucesorio), SUC_200 (Publicación de edictos y plazo de citación de herederos y acreedores)

### D08 · Testamento ológrafo

El CPCCBA (art. 739) pide dos testigos que reconozcan la letra y la firma; el CCyC (art. 2339) exige pericia caligráfica. ¿Qué se hace en la práctica: audiencia con testigos, pericia o ambas? ¿La audiencia es FECHA_FIJADA o depende de la pericia?

**Hitos afectados:** SUC_150 (Audiencia de reconocimiento del testamento ológrafo o cerrado), SUC_160 (Protocolización del testamento o agregación del testimonio)

### D09 · Testamento cerrado

El CCyC solo admite las formas que regula (art. 2473): el ológrafo y el acto público. ¿Un testamento cerrado solo puede valer si se otorgó antes del 01/08/2015 o en el extranjero (art. 2645 CCyC)? ¿El art. 739 CPCCBA sigue aplicándose a esos casos?

**Hitos afectados:** SUC_040 (Búsqueda de testamento), SUC_150 (Audiencia de reconocimiento del testamento ológrafo o cerrado)

### D10 · Ministerio Público

¿En qué casos interviene en el sucesorio en PBA: la Asesoría de Incapaces siempre que haya menores o personas con capacidad restringida (art. 103 CCyC), y el agente fiscal en las vacantes o con ausentes? ¿Con qué norma orgánica (Ley 14.442, a verificar)? El art. 728 inc. 1 CPCCBA dice que cesa con la declaratoria. ¿Hay un plazo para contestar sus observaciones?

**Hitos afectados:** SUC_140 (Vista al Ministerio Público), SUC_350 (Herencia vacante y designación del curador)

### D11 · Intervención de ARBA

El art. 728 inc. 3 CPCCBA da intervención al organismo recaudador por el ITGB. ¿Se le da vista en el expediente? ¿Puede oponerse a la denuncia de bienes (art. 751) y en qué plazo?

**Hitos afectados:** SUC_510 (Denuncia de bienes y valuación por los herederos), SUC_910 (Declaración jurada y pago del ITGB ante ARBA)

### D13 · Declaratoria de herederos

¿Qué requisitos controlan los juzgados antes de dictarla (edictos, cédulas, informes de los registros, partidas)? ¿Hay un plazo para que el juez la dicte, para alertar demoras?

**Hitos afectados:** SUC_300 (Pedido de la declaratoria de herederos), SUC_310 (Dictado de la declaratoria de herederos)

### D14 · Recursos contra la declaratoria

¿La declaratoria y la aprobación del testamento se apelan en 5 días, con concesión en relación y memorial en otros 5 (arts. 243, 244 y 246 CPCCBA)? ¿Procede la aclaratoria del art. 166 inc. 2 para errores de nombres o documentos, y suspende el plazo de la apelación?

**Hitos afectados:** SUC_310 (Dictado de la declaratoria de herederos), SUC_320 (Aprobación formal del testamento), SUC_810 (Apelación de una resolución del sucesorio), SUC_815 (Memorial de la apelación en relación)

### D15 · Impugnación de la declaratoria

La impugnación del art. 737 CPCCBA y la petición de herencia (art. 2311 CCyC: imprescriptible), ¿tramitan por juicio ordinario ante el juez del sucesorio? ¿Qué plazo de contestación corresponde cargar?

**Hitos afectados:** SUC_860 (Impugnación de la declaratoria o petición de herencia)

### D18 · Acreedores que promueven el sucesorio

El art. 729 CPCCBA permite a los acreedores iniciar el sucesorio pasados 4 meses del fallecimiento (el juez puede ampliar o reducir el plazo). La norma cita el art. 3314 del Código Civil derogado. ¿Conviene un hito propio (MESES, 4) o alcanza con el aviso del checklist?

**Hitos afectados:** SUC_010 (Consulta inicial por el fallecimiento del causante)

### D20 · Venta de bienes

El CCyC (art. 2353) permite vender con acuerdo unánime o autorización judicial; el CPCCBA (art. 747) limita al administrador a actos conservatorios. ¿Qué exigen los juzgados en la práctica (tasación, vista al Ministerio Público, subasta o venta privada)?

**Hitos afectados:** SUC_440 (Pago de deudas y legados, y venta de bienes con autorización)

### D22 · Denuncia de bienes

¿La denuncia de bienes se pone de manifiesto 5 días, como el inventario y avalúo (art. 759 CPCCBA)? ¿Qué valuación aceptan los juzgados (fiscal, art. 758)? La matriz la hace pasar por el mismo traslado.

**Hitos afectados:** SUC_510 (Denuncia de bienes y valuación por los herederos), SUC_530 (Traslado del inventario y avalúo o de la denuncia de bienes)

### D23 · Cónyuge supérstite y gananciales

¿Cómo se trata la indivisión poscomunitaria dentro del sucesorio (art. 481 CCyC): quién califica los bienes, si hace falta acuerdo expreso con el cónyuge y cómo impacta en la tasa (art. 337 inc. f Código Fiscal) y en los honorarios (art. 35 Ley 14.967, que incluye los gananciales en la base)?

**Hitos afectados:** SUC_520 (Liquidación de los gananciales con el cónyuge supérstite), SUC_900 (Pago de la tasa de justicia y de la contribución para la Caja de Abogados), SUC_920 (Regulación de honorarios)

### D24 · Unión convivencial

El conviviente no hereda, pero puede invocar el derecho real de habitación gratuito por hasta 2 años (art. 527 CCyC). ¿Hace falta un hito propio en la V1? Propuesta: aviso en el checklist y plazo suelto.

**Hitos afectados:** SUC_010 (Consulta inicial por el fallecimiento del causante), SUC_330 (Elección del trámite posterior a la declaratoria o a la aprobación del testamento)

### D25 · Partición

Privada (art. 2369 CCyC y 761 CPCCBA): ¿cómo se instrumenta (escrito con firmas certificadas, escritura) y se aprueba? Judicial: el traslado de la cuenta particionaria es de 10 días (art. 766), ¿hábiles y con gracia? Licitación (art. 2372 CCyC: 30 días desde la aprobación de la tasación): ¿conviene un hito propio?

**Hitos afectados:** SUC_540 (Aprobación del inventario y avalúo), SUC_600 (Partición privada), SUC_610 (Designación del partidor y presentación de la cuenta particionaria), SUC_620 (Traslado de la cuenta particionaria)

### D26 · Colación y reducción

¿Qué vía procesal y qué prescripción rigen para la colación (¿el plazo genérico de 5 años del art. 2560 CCyC, o se reclama dentro de la partición, que es imprescriptible mientras dure la indivisión según el art. 2368?) y para la reducción (art. 2459 CCyC: no procede contra el donatario que poseyó 10 años)? ¿Se reclama dentro del sucesorio o en juicio aparte?

**Hitos afectados:** SUC_650 (Colación y reducción para proteger la legítima)

### D27 · Trámite extrajudicial

¿Se usa el art. 733 CPCCBA en la práctica? ¿Qué organismos intervienen y cómo se acredita su conformidad?

**Hitos afectados:** SUC_660 (Continuación extrajudicial del sucesorio)

### D28 · Tasa de justicia

Según el Código Fiscal, se paga al pedir la inscripción (art. 338 inc. c) sobre la valuación vigente a la fecha del auto que la ordena (art. 332), sin la parte ganancial del cónyuge (art. 337 inc. f); así lo aplicó la Cám. Civ. y Com. Trenque Lauquen el 11/04/2024. ¿Algún juzgado exige un pago a cuenta al inicio? ¿La alícuota de la Ley Impositiva 2026 (Ley 15.558) es 22 por mil y se presume un 10% de otros bienes? La contribución para la Caja de Abogados es del 5% de la tasa en el texto vigente del art. 12 inc. g Ley 6716 (normas.gba.gob.ar); fuentes anteriores dicen 10%.

**Hitos afectados:** SUC_100 (Escrito de inicio del sucesorio), SUC_700 (Pedido de la orden de inscripción), SUC_900 (Pago de la tasa de justicia y de la contribución para la Caja de Abogados)

### D29 · Bono y anticipo previsional

El bono de la Ley 8480 y el jus previsional del art. 13 de la Ley 6716 se pagan al iniciar. ¿Por cada letrado? ¿Cada heredero que se presenta con otro abogado paga los suyos?

**Hitos afectados:** SUC_100 (Escrito de inicio del sucesorio)

### D32 · Inscripción de bienes

¿Qué recaudos exigen hoy el Registro de la Propiedad Inmueble de PBA (testimonio o minuta, tasas, vigencia de los certificados), el DNRPA (solicitud tipo), los bancos y las sociedades (libro de accionistas, DPPJ)? Ver el Decreto-Ley 11.643/63 y la Ley 17.801.

**Hitos afectados:** SUC_740 (Orden de inscripción y libramiento de oficios y testimonios), SUC_750 (Inscripción en el Registro de la Propiedad Inmueble de PBA), SUC_752 (Inscripción de automotores en el DNRPA), SUC_754 (Transferencia de fondos y de participaciones societarias)

### D33 · Tracto abreviado

¿Qué inciso del art. 16 de la Ley 17.801 se aplica a la venta por los herederos declarados y qué requisitos pide el Registro de PBA?

**Hitos afectados:** SUC_756 (Venta por los herederos con tracto abreviado)

### D34 · Bienes en otra jurisdicción

Confirmar la adhesión de PBA y de las jurisdicciones de destino a la Ley 22.172 y los recaudos (letrado autorizado, tasas y aportes locales). ¿También se paga allí tasa de justicia?

**Hitos afectados:** SUC_200 (Publicación de edictos y plazo de citación de herederos y acreedores), SUC_758 (Inscripción de bienes en otra jurisdicción por oficio Ley 22.172)

### D35 · Causante extranjero o con bienes en el exterior

Arts. 2643 a 2648 CCyC. ¿Conviene un flujo aparte cuando el causante tenía domicilio en el exterior, o alcanza con el checklist de la competencia? ¿Cómo se acreditan las partidas y los testamentos extranjeros?

**Hitos afectados:** SUC_030 (Último domicilio del causante y juzgado competente), SUC_040 (Búsqueda de testamento)

## 6. Bloque D · Producto

Las responde el equipo técnico, no el abogado. Solo quedan registradas: no se modificó el contrato de API ni el modelo de datos.

### D41 · Producto: roles del sucesorio

El enum Rol_Responsable (ACTORA, DEMANDADA, TRIBUNAL, AMBAS) se usó así: ACTORA, el heredero que promueve y al que representamos; DEMANDADA, otros interesados con intereses opuestos; TRIBUNAL, el juzgado o un organismo; AMBAS, cualquier interesado. ¿Hacen falta roles propios del sucesorio, como INTERESADO u ORGANISMO? Propuesta para la V1: mantener el enum y aclarar en el nombre del hito.

**Hitos afectados:** Todos

### D42 · Producto: rol representado

legal_cases.represented_role solo admite ACTORA o DEMANDADA, pero el sucesorio no tiene demandado. Si representamos a un coheredero que impugna, al cónyuge en la liquidación de gananciales o al heredero intimado a aceptar, las alertas de 'te toca a vos' quedan invertidas. ¿Se elige DEMANDADA en esos casos, se agrega un valor nuevo o el rol se define por hito? Solo se registra; no se modifica el contrato de API.

**Hitos afectados:** SUC_230 (Intimación a un heredero a aceptar o renunciar la herencia), SUC_520 (Liquidación de los gananciales con el cónyuge supérstite), SUC_850 (Acción de nulidad o impugnación del testamento), SUC_860 (Impugnación de la declaratoria o petición de herencia)

### D43 · Producto: flujo prejudicial y judicial

La fase Previa (SUC_010 a SUC_050) va al flujo PREJUDICIAL. Pero SUC_015 (10 años) y SUC_016 (24 meses del ITGB) corren desde la muerte y siguen durante el juicio, y SUC_016 lleva a SUC_910, que es del flujo judicial. ¿Cómo se conservan esos plazos al pasar al flujo judicial? ¿Se admite una transición entre flujos, como en el laboral?

**Hitos afectados:** SUC_010 (Consulta inicial por el fallecimiento del causante), SUC_015 (Control de la caducidad del derecho de aceptar la herencia), SUC_016 (Vencimiento máximo del ITGB: 24 meses desde el fallecimiento), SUC_020 (Reunión de las partidas que acreditan el fallecimiento y el vínculo), SUC_030 (Último domicilio del causante y juzgado competente), SUC_040 (Búsqueda de testamento), SUC_050 (Relevamiento del acervo: bienes y deudas), SUC_910 (Declaración jurada y pago del ITGB ante ARBA)

### D44 · Producto: catálogos

El catálogo de regímenes solo tiene PBA_LAB_LEY_11653 y PBA_LAB_LEY_15057; hace falta uno civil (por ejemplo, PBA_CIV_DL_7425) y el fuero CIVIL_COMERCIAL en legal_branches. Además, courts.court_type (TRIBUNAL_TRABAJO, JUZGADO_LABORAL, CAMARA_APELACION) no tiene Juzgado Civil y Comercial ni Juzgado de Paz Letrado, y legal_cases.closed_reason no tiene un motivo para la sucesión terminada por inscripción. Solo se registra; no se modifican el contrato de API ni el modelo de datos.

**Hitos afectados:** Todos

### D45 · Producto: caminos que deben esperar a otros

La app abre caminos en paralelo, pero no tiene un hito que espere a que terminen todos. Por ejemplo, la declaratoria necesita la citación vencida y el informe del Registro de Juicios Universales, y la orden de inscripción necesita la tasa, el ITGB, los honorarios y los aportes pagados. Propuesta para la V1: lo controla el checklist; evaluar para la V2 una espera explícita.

**Hitos afectados:** SUC_300 (Pedido de la declaratoria de herederos), SUC_740 (Orden de inscripción y libramiento de oficios y testimonios)

## 7. Citas marcadas "(a verificar)" en los hitos

No se pudieron confirmar en una fuente oficial o actualizada al 13/11/2026. Cada una se confirma o se corrige en la columna `Base_Normativa` o en el checklist del hito.

| Hito | Nombre | Texto |
| :--- | :--- | :--- |
| SUC_040 | Búsqueda de testamento | Si el causante vivió o testó en otra jurisdicción, evaluar pedir informe al registro de esa jurisdicción (a verificar cuál) |
| SUC_140 | Vista al Ministerio Público | Art. 103 CCyC; art. 728 inc. 1 CPCCBA; Ley 14.442 (a verificar) |
| SUC_600 | Partición privada | Instrumentar el acuerdo y presentarlo para su aprobación (forma a verificar, duda D25) |
| SUC_740 | Orden de inscripción y libramiento de oficios y testimonios | Preparar el testimonio para el Registro de la Propiedad Inmueble con los recaudos que exija (a verificar) |
| SUC_752 | Inscripción de automotores en el DNRPA | Decreto-Ley 6582/58 y normas técnico-registrales del DNRPA (a verificar) |
| SUC_752 | Inscripción de automotores en el DNRPA | Usar la solicitud tipo que indique el Registro (a verificar) |
| SUC_754 | Transferencia de fondos y de participaciones societarias | Art. 725 CPCCBA; art. 17 Ley 6716 (a verificar); Ley General de Sociedades 19.550 (artículos a verificar) |
| SUC_756 | Venta por los herederos con tracto abreviado | Art. 16 Ley 17.801 (inciso a verificar) |
| SUC_758 | Inscripción de bienes en otra jurisdicción por oficio Ley 22.172 | Ley 22.172 (adhesión de PBA y de la jurisdicción de destino a verificar) |
| SUC_900 | Pago de la tasa de justicia y de la contribución para la Caja de Abogados | Liquidar sobre el valor del activo, sin la parte ganancial del cónyuge supérstite (art. 337 inc. f Código Fiscal), con la alícuota de la Ley Impositiva vigente (a verificar: 22 por mil) |
| SUC_910 | Declaración jurada y pago del ITGB ante ARBA | Pagar o adherir a un plan de pagos (a verificar) |
| SUC_810 | Apelación de una resolución del sucesorio | Si la resolución tiene errores materiales (por ejemplo, nombres o documentos en la declaratoria), pedir aclaratoria dentro de los 3 días (art. 166 inc. 2; aplicación a la declaratoria a verificar) |
| SUC_870 | Control de la caducidad de instancia en un incidente con controversia | Arts. 310, 311 y 313 inc. 2 CPCCBA (plazo de los incidentes a verificar) |

## 8. Después de validar

1. Pasar a `VALIDADO` o `CORREGIR` cada duda, hito y transición.
2. Completar en la hoja `Flujo` quién validó y la fecha.
3. Regenerar solo el diagrama desde la planilla, con `diagrama.py` (ver [`README.md`](README.md)).
4. Llevar las respuestas de producto (bloque D) al equipo técnico.

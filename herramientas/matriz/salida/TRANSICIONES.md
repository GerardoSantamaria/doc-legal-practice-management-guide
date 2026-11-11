| ID_Paso_Origen | Condicion_Salida | ID_Paso_Destino |
| ----- | ----- | ----- |
| **LAB_010** | Despido directo comunicado por el empleador | **LAB_015** (Control de prescripción de la acción) |
| **LAB_010** | Despido directo comunicado por el empleador | **LAB_016** (Entrega de certificados de trabajo) |
| **LAB_010** | Despido directo comunicado por el empleador | **LAB_020** (Pago de la liquidación final e indemnizaciones) |
| **LAB_010** | Injuria del empleador con el vínculo vigente | **LAB_030** (Intimación telegráfica del trabajador) |
| **LAB_015** | Demanda interpuesta en término | `CIERRA_CAMINO` |
| **LAB_016** | Certificados entregados | `CIERRA_CAMINO` |
| **LAB_016** | No entregados en 30 días | **LAB_017** (Intimación de entrega de certificados) |
| **LAB_017** | Certificados entregados | `CIERRA_CAMINO` |
| **LAB_017** | No entregados: se reclaman en la demanda | `CIERRA_CAMINO` |
| **LAB_020** | Pago íntegro, sin reclamo pendiente | **LAB_990** (Archivo del expediente) |
| **LAB_020** | Falta de pago o pago insuficiente | **LAB_030** (Intimación telegráfica del trabajador) |
| **LAB_030** | El empleador regulariza o paga | **LAB_990** (Archivo del expediente) |
| **LAB_030** | Rechazo o silencio con el vínculo vigente | **LAB_035** (Comunicación del despido indirecto) |
| **LAB_030** | Rechazo o silencio con el vínculo ya extinguido | **LAB_040** (Instancia de conciliación laboral previa) |
| **LAB_035** | Despido indirecto comunicado | **LAB_015** (Control de prescripción de la acción) |
| **LAB_035** | Despido indirecto comunicado | **LAB_016** (Entrega de certificados de trabajo) |
| **LAB_035** | Despido indirecto comunicado | **LAB_040** (Instancia de conciliación laboral previa) |
| **LAB_040** | Acuerdo alcanzado | **LAB_900** (Acuerdo conciliatorio y homologación) |
| **LAB_040** | Fracaso de la conciliación o instancia no exigida | **LAB_050** (Interposición de la demanda) |
| **LAB_050** | Demanda interpuesta | **LAB_060** (Radicación y traslado de la demanda) |
| **LAB_060** | Se ordena subsanar defectos | **LAB_065** (Subsanación de defectos de la demanda) |
| **LAB_060** | Se ordena el traslado de la demanda | **LAB_070** (Contestación de la demanda) |
| **LAB_065** | Defectos subsanados en término | **LAB_070** (Contestación de la demanda) |
| **LAB_065** | No subsanados: se tiene por no presentada | **LAB_990** (Archivo del expediente) |
| **LAB_070** | Contesta la demanda (con o sin excepciones) | **LAB_080** (Traslado al actor de la contestación, documental y excepciones) |
| **LAB_070** | Contesta y reconviene | **LAB_080** (Traslado al actor de la contestación, documental y excepciones) |
| **LAB_070** | Contesta y reconviene | **LAB_085** (Contestación de la reconvención) |
| **LAB_070** | No contesta en término | **LAB_075** (Demanda no contestada) |
| **LAB_075** | Se tiene por no contestada la demanda | **LAB_100** (Auto de apertura a prueba) |
| **LAB_080** | Hay excepciones de previo y especial pronunciamiento | **LAB_090** (Resolución de excepciones de previo pronunciamiento) |
| **LAB_080** | Sin excepciones de previo pronunciamiento | **LAB_100** (Auto de apertura a prueba) |
| **LAB_085** | Reconvención contestada o plazo vencido | `CIERRA_CAMINO` |
| **LAB_090** | Excepciones rechazadas | **LAB_100** (Auto de apertura a prueba) |
| **LAB_090** | Excepción admitida que pone fin al proceso | **LAB_700** (Recurso extraordinario ante la SCBA) |
| **LAB_100** | Se provee toda la prueba ofrecida | **LAB_110** (Producción de la prueba pericial) |
| **LAB_100** | Se provee toda la prueba ofrecida | **LAB_120** (Producción de la prueba informativa) |
| **LAB_100** | Se provee toda la prueba ofrecida | **LAB_200** (Fijación de la audiencia de vista de causa) |
| **LAB_100** | Se deniega parte de la prueba ofrecida | **LAB_105** (Reposición contra la denegatoria de prueba) |
| **LAB_100** | Se deniega parte de la prueba ofrecida | **LAB_110** (Producción de la prueba pericial) |
| **LAB_100** | Se deniega parte de la prueba ofrecida | **LAB_120** (Producción de la prueba informativa) |
| **LAB_100** | Se deniega parte de la prueba ofrecida | **LAB_200** (Fijación de la audiencia de vista de causa) |
| **LAB_100** | Causa declarada de puro derecho | **LAB_600** (Veredicto y sentencia) |
| **LAB_105** | Reposición resuelta o plazo vencido | `CIERRA_CAMINO` |
| **LAB_110** | Dictamen pericial presentado | **LAB_115** (Traslado del dictamen pericial) |
| **LAB_110** | No se ofreció pericial o fue desistida | `CIERRA_CAMINO` |
| **LAB_115** | Se impugna o se piden explicaciones | **LAB_117** (Respuesta del perito a las observaciones) |
| **LAB_115** | Sin observaciones | `CIERRA_CAMINO` |
| **LAB_117** | El perito contesta las observaciones | `CIERRA_CAMINO` |
| **LAB_120** | Informes contestados o prueba desistida | `CIERRA_CAMINO` |
| **LAB_200** | Audiencia de vista de causa fijada | **LAB_210** (Audiencia de vista de causa) |
| **LAB_210** | Audiencia realizada; causa en estado de veredicto | **LAB_600** (Veredicto y sentencia) |
| **LAB_210** | Audiencia suspendida o reprogramada | **LAB_200** (Fijación de la audiencia de vista de causa) |
| **LAB_210** | Acuerdo conciliatorio en la audiencia | **LAB_900** (Acuerdo conciliatorio y homologación) |
| **LAB_600** | Veredicto y sentencia notificados | **LAB_610** (Aclaratoria) |
| **LAB_600** | Veredicto y sentencia notificados | **LAB_700** (Recurso extraordinario ante la SCBA) |
| **LAB_600** | Veredicto y sentencia notificados | **LAB_850** (Impugnación de la regulación de honorarios) |
| **LAB_610** | Aclaratoria resuelta o plazo vencido | `CIERRA_CAMINO` |
| **LAB_700** | No se recurre: sentencia firme con condena | **LAB_800** (Liquidación de la condena) |
| **LAB_700** | No se recurre: sentencia firme sin condena a pagar | **LAB_990** (Archivo del expediente) |
| **LAB_700** | Se interpone recurso extraordinario | **LAB_710** (Concesión del recurso) |
| **LAB_710** | Recurso concedido | **LAB_730** (Trámite y resolución ante la SCBA) |
| **LAB_710** | Recurso denegado | **LAB_720** (Queja por recurso denegado) |
| **LAB_720** | Queja admitida | **LAB_730** (Trámite y resolución ante la SCBA) |
| **LAB_720** | Queja rechazada o no interpuesta: sentencia firme | **LAB_800** (Liquidación de la condena) |
| **LAB_730** | La SCBA resuelve: sentencia firme con condena | **LAB_800** (Liquidación de la condena) |
| **LAB_730** | La SCBA resuelve: sin condena a pagar | **LAB_990** (Archivo del expediente) |
| **LAB_730** | La SCBA anula y reenvía para nuevo pronunciamiento | **LAB_600** (Veredicto y sentencia) |
| **LAB_800** | Liquidación aprobada | **LAB_810** (Depósito de la condena) |
| **LAB_810** | Depósito en término | **LAB_830** (Cobro y rendición al cliente) |
| **LAB_810** | Falta de depósito | **LAB_820** (Ejecución de la sentencia) |
| **LAB_820** | Fondos embargados o depositados | **LAB_830** (Cobro y rendición al cliente) |
| **LAB_830** | Cobro percibido y rendido al cliente | **LAB_990** (Archivo del expediente) |
| **LAB_850** | Regulación firme o impugnación resuelta | `CIERRA_CAMINO` |
| **LAB_900** | Acuerdo homologado | **LAB_910** (Cumplimiento del acuerdo) |
| **LAB_910** | Acuerdo cumplido | **LAB_990** (Archivo del expediente) |
| **LAB_910** | Acuerdo incumplido | **LAB_820** (Ejecución de la sentencia) |

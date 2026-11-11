// Genera las capturas PNG de las maquetas de diseno/pantallas/.
// Uso: npm run capturar [-- archivo.html ...] (ver herramientas/README.md).
const path = require('path');
const fs = require('fs');
const puppeteer = require('puppeteer');

const RAIZ = path.resolve(__dirname, '..', '..');
const PANTALLAS = path.join(RAIZ, 'diseno', 'pantallas');
const SALIDA = path.join(PANTALLAS, 'capturas');

const ESCRITORIO = { width: 1440, height: 900 };
const CELULAR = { width: 390, height: 844 };

const CAPTURAS = {
  '01_ingreso.html': [ESCRITORIO, CELULAR],
  '02_bienvenida.html': [ESCRITORIO],
  '03_inicio.html': [ESCRITORIO, CELULAR],
  '04_expedientes.html': [ESCRITORIO, CELULAR],
  '05_nuevo_expediente.html': [ESCRITORIO, CELULAR],
  '06_nuevo_en_curso.html': [ESCRITORIO],
  '07_ficha.html': [ESCRITORIO, CELULAR],
  '08_dialogos.html': [ESCRITORIO],
  '09_clientes.html': [ESCRITORIO],
  '10_calendario.html': [ESCRITORIO],
  '11_cuenta_plan.html': [ESCRITORIO],
  '12_cuenta_facturacion.html': [ESCRITORIO],
  '13_cuenta_equipo.html': [ESCRITORIO],
  '14_cuenta_avisos.html': [ESCRITORIO],
  '15_estados.html': [ESCRITORIO],
  '16_admin_calendario.html': [ESCRITORIO],
  '17_admin_matriz.html': [ESCRITORIO],
  '18_email_resumen.html': [{ width: 720, height: 900 }],
};

(async () => {
  const pedidos = process.argv.slice(2);
  const archivos = pedidos.length ? pedidos : Object.keys(CAPTURAS);
  fs.mkdirSync(SALIDA, { recursive: true });
  const navegador = await puppeteer.launch({ headless: true, args: ['--allow-file-access-from-files'] });
  try {
    const pagina = await navegador.newPage();
    for (const archivo of archivos) {
      const tamanos = CAPTURAS[archivo];
      if (!tamanos) throw new Error(`Maqueta desconocida: ${archivo}`);
      for (const tamano of tamanos) {
        await pagina.setViewport({ ...tamano, deviceScaleFactor: 1 });
        await pagina.goto('file://' + path.join(PANTALLAS, archivo), { waitUntil: 'networkidle0' });
        // La ventana toma el alto de la página para que la barra inferior fija quede al final de la captura.
        const alto = await pagina.evaluate(() => document.documentElement.scrollHeight);
        await pagina.setViewport({ width: tamano.width, height: Math.max(alto, tamano.height), deviceScaleFactor: 1 });
        const sufijo = tamano.width < 600 ? '_celular' : '';
        const destino = path.join(SALIDA, archivo.replace('.html', `${sufijo}.png`));
        await pagina.screenshot({ path: destino });
        console.log('OK', path.relative(RAIZ, destino));
      }
    }
  } finally {
    await navegador.close();
  }
})();

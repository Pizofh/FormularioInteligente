import { Page, Locator } from '@playwright/test';

export class DatosPersonalesPage {
  readonly page: Page;
  readonly tab: Locator;

  readonly primer_nombre: Locator;
  readonly segundo_nombre: Locator;
  readonly primer_apellido: Locator;
  readonly segundo_apellido: Locator;
  readonly tipo_documento: Locator;
  readonly numero_documento: Locator
  readonly fecha_expedición: Locator;
  readonly lugar_expedición: Locator;
  readonly pasaporte_numero: Locator;
  readonly fecha_pasaporte: Locator;
  readonly dia_nacimiento: Locator;
  readonly mes_nacimiento: Locator;
  readonly año_nacimiento: Locator;
  readonly estado_civil: Locator;
  readonly profesion_oficio: Locator;
  readonly tarjeta_profesional: Locator;
  readonly señales_corporales: Locator;
  readonly estatura: Locator; 
  readonly peso: Locator; 
  readonly tipo_via: Locator; 
  readonly numero_principal: Locator; 
  readonly letra_principal: Locator; 
  readonly bis: Locator; 
  readonly letra_bis: Locator; 
  readonly cuadrante: Locator; 
  readonly numero_secundario: Locator;
  readonly letra_secundaria: Locator; 
  readonly cuadrante_dos: Locator;
  readonly nro: Locator; 
  readonly complemento: Locator; 
  readonly barrio: Locator; 
  readonly numero_celular: Locator;
  readonly telefono_fijo: Locator; 
  readonly ciudad: Locator;
  readonly departamento: Locator; 
  readonly correo_electronico_personal: Locator; 
  readonly direccion_formateada: Locator; 


  constructor(page: Page) {
    this.page = page;
    this.tab = page.locator('text=Datos Personales');

    this.primer_nombre = page.locator('#id_recluta-primer_nombre');
    this.segundo_nombre = page.locator('#id_recluta-segundo_nombre');
    this.primer_apellido = page.locator('#id_recluta-primer_apellido');
    this.segundo_apellido = page.locator('#id_recluta-segundo_apellido');
    this.tipo_documento = page.locator('#id_recluta-tipo_documento');
    this.numero_documento = page.locator('#id_recluta-numero_documento');
    this.fecha_expedición = page.locator('#id_recluta-fecha_expedición');
    this.lugar_expedición = page.locator('#id_recluta-lugar_expedición')
    this.pasaporte_numero  = page.locator('#id_recluta-pasaporte_numero');
    this.fecha_pasaporte = page.locator('#id_recluta-fecha_pasaporte');

    this.dia_nacimiento = page.locator('#id_recluta-dia_nacimiento');
    this.mes_nacimiento = page.locator('#id_recluta-mes_nacimiento');
    this.año_nacimiento = page.locator('#id_recluta-año_nacimiento');
    this.estado_civil = page.locator('#id_recluta-estado_civil');
    this.profesion_oficio = page.locator('#id_recluta-profesion_oficio');
    this.tarjeta_profesional = page.locator('#id_recluta-tarjeta_profesional');
    this.señales_corporales = page.locator('#id_recluta-señales_corporales');
    this.estatura = page.locator('#id_recluta-estatura');
    this.peso = page.locator('#id_recluta-peso');
    this.tipo_via = page.locator('#id_recluta-tipo_via');
    this.numero_principal = page.locator('#id_recluta-numero_principal');
    this.letra_principal = page.locator('#id_recluta-letra_principal');
    this.bis = page.locator('#id_recluta-bis');
    this.letra_bis = page.locator('#id_recluta-letra_bis');
    this.cuadrante = page.locator('#id_recluta-cuadrante');
    this.numero_secundario = page.locator('#id_recluta-numero_secundario');
    this.letra_secundaria = page.locator('#id_recluta-letra_secundaria');
    this.cuadrante_dos = page.locator('#id_recluta-cuadrante_dos');
    this.nro = page.locator('#id_recluta-nro');
    this.complemento = page.locator('#id_recluta-complemento');
    this.barrio = page.locator('#id_recluta-barrio');
    this.numero_celular = page.locator('#id_recluta-numero_celular');
    this.telefono_fijo = page.locator('#id_recluta-telefono_fijo');
    this.ciudad = page.locator('#id_recluta-ciudad');
    this.departamento = page.locator('#id_recluta-departamento');
    this.correo_electronico_personal = page.locator('#id_recluta-correo_electronico_personal');
    this.direccion_formateada = page.locator('#direccion-preview');
  }


  async llenarFormulario() {

        function generarNumeroAleatorio(digitos: number): string {
    const min = Math.pow(10, digitos - 1);
    const max = Math.pow(10, digitos) - 1;
    return Math.floor(Math.random() * (max - min + 1)) + min + '';
  }

    const documentoUnico = generarNumeroAleatorio(10);
    const celularUnico = '3' + generarNumeroAleatorio(9);
    await this.primer_nombre.fill('Brian');
    await this.segundo_nombre.fill('Steve');
    await this.primer_apellido.fill('Garnica');
    await this.segundo_apellido.fill('Sandoval');
    await this.tipo_documento.selectOption('CC');
    await this.numero_documento.fill(documentoUnico);
    await this.fecha_expedición.fill('2018-08-14');
    await this.lugar_expedición.fill('Bogotá');
    await this.pasaporte_numero.fill('Num123456');
    await this.fecha_pasaporte.fill('2019-05-04');

    await this.dia_nacimiento.selectOption('12');
    await this.mes_nacimiento.selectOption('8');
    await this.año_nacimiento.fill('2000');
    await this.estado_civil.selectOption('Soltero(a)');
    await this.profesion_oficio.fill('Ingeniero Aeronáutico');
    await this.tarjeta_profesional.fill('IA123456');
    await this.señales_corporales.fill('Tatuajes en varias zonas del cuerpo como: a, b, c');
    await this.estatura.fill('170');
    await this.peso.fill('67')
    await this.tipo_via.selectOption('Carrera');
    await this.numero_principal.fill('69');
    await this.letra_principal.selectOption('C');
    await this.bis.check();
    await this.letra_bis.selectOption('A');
    await this.cuadrante.selectOption('ESTE');
    await this.numero_secundario.fill('69');
    await this.letra_secundaria.selectOption('H');
    await this.cuadrante_dos.selectOption('ESTE');
    await this.nro.fill('22');
    await this.complemento.fill('Segundo Piso');
    await this.barrio.fill('La estrada');
    await this.numero_celular.fill(celularUnico);
    await this.telefono_fijo.fill('7523491');
    await this.ciudad.fill('Tunja');
    await this.departamento.fill('Boyacá');
    await this.correo_electronico_personal.fill('stevegarasdnicas@hotmail.com');
  } 

  async obtenerDireccionFormateadaRecluta(): Promise<string> {
  const DireccionFormateadaRecluta = await this.direccion_formateada.textContent();
  return DireccionFormateadaRecluta?.trim() ?? '';
}

  getErrorMessageForField(fieldId: string): Locator {
    return this.page.locator(`#${fieldId}_error strong`);
  }


  async FillFormWithErrors() {

  function generarNumeroAleatorio(): string {
  const numero = Math.floor(Math.random() * 1000); // entre 0 y 999
  return numero.toString();
}

    const wrongdocument = generarNumeroAleatorio();
    const wrongphone = generarNumeroAleatorio();
    await this.primer_nombre.fill('123');
    await this.segundo_nombre.fill('123');
    await this.primer_apellido.fill('123');
    await this.segundo_apellido.fill('123');
    await this.tipo_documento.selectOption('CC');
    await this.numero_documento.fill(wrongdocument);
    await this.fecha_expedición.fill('2018-08-14');
    await this.lugar_expedición.fill('123');
    await this.pasaporte_numero.fill('x#$"%&%YRTGERFEDC');
    await this.fecha_pasaporte.fill('2019-05-04');
    await this.dia_nacimiento.selectOption('12');
    await this.mes_nacimiento.selectOption('8');
    await this.año_nacimiento.fill('999999999');
    await this.estado_civil.selectOption('Soltero(a)');
    await this.profesion_oficio.fill('ADFV3"$RR$#%#EREADSFG#"4234SDF');
    await this.tarjeta_profesional.fill('IA12"#"$%$&%YU/&&%3456');
    await this.señales_corporales.fill('FGBHGNJKIU(/&%$#"WQSASDCFV');
    await this.estatura.fill('1');
    await this.peso.fill('999999')
    await this.tipo_via.selectOption('Carrera');
    await this.numero_principal.fill('622222222222222229');
    await this.letra_principal.selectOption('C');
    await this.bis.check();
    await this.letra_bis.selectOption('A');
    await this.cuadrante.selectOption('ESTE');
    await this.numero_secundario.fill('6999999999999999999999');
    await this.letra_secundaria.selectOption('H');
    await this.cuadrante_dos.selectOption('ESTE');
    await this.nro.fill('299999999992');
    await this.complemento.fill('SADFWR#$T%$#%$WREGFH5');
    await this.barrio.fill('!#$"%#$Y&%HGFBVDS');
    await this.numero_celular.fill(wrongphone);
    await this.telefono_fijo.fill('1');
    await this.ciudad.fill('123a#');
    await this.departamento.fill('123213rewRF#"$');
    await this.correo_electronico_personal.fill('steve');
  } 



}
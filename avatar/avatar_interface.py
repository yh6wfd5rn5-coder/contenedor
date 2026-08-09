#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INTERFAZ DE CONTROL DEL AVATAR
Panel para interactuar con el avatar ARIA
"""

import json
import sys
from typing import Dict, List, Any
from datetime import datetime
try:
    from quantum_engine import MotorCuanticoCentral
except ImportError:
    print("⚠️  Módulos cuánticos no disponibles en modo simulación")
    MotorCuanticoCentral = None


class InterfazAvatar:
    """Interfaz de usuario/IA para controlar el avatar ARIA"""
    
    def __init__(self, nombre_avatar: str = "ARIA"):
        self.nombre_avatar = nombre_avatar
        if MotorCuanticoCentral:
            self.motor = MotorCuanticoCentral(nombre_avatar)
        else:
            self.motor = None
        self.historial = []
        self.conectado = True
        
    def ejecutar_comando(self, comando: str) -> Dict[str, Any]:
        """Ejecutar comando del usuario"""
        if not self.motor:
            return self._simular_comando(comando)
        
        resultado = self.motor.operar(comando)
        self.historial.append({
            "comando": comando,
            "resultado": resultado,
            "timestamp": datetime.now().isoformat()
        })
        return resultado
    
    def _simular_comando(self, comando: str) -> Dict[str, Any]:
        """Simular ejecución de comando (modo sin importar módulos)"""
        return {
            "estado": "simulado",
            "comando": comando,
            "timestamp": datetime.now().isoformat(),
            "resultado": f"Simulado: {comando}"
        }
    
    def ver_estado(self) -> Dict[str, Any]:
        """Ver estado actual del avatar"""
        if self.motor:
            return self.motor.status()
        return {"estado": "no_inicializado", "conexión": "simulada"}
    
    def ver_pantalla_interna(self) -> Dict[str, Any]:
        """Ver lo que está creando el avatar"""
        if self.motor:
            return self.motor.creación.pantalla_interna()
        return {"pantalla": "no_disponible"}
    
    def ver_visión(self) -> Dict[str, Any]:
        """Ver análisis visual del avatar"""
        if self.motor:
            return self.motor.visión.analizar_repositorio(".")
        return {"análisis": "no_disponible"}
    
    def ver_audición(self) -> Dict[str, Any]:
        """Ver estado de audición"""
        if self.motor:
            return {
                "estado": "escuchando",
                "comandos_procesados": len(self.motor.audición.comandos_procesados),
                "comandos_en_cola": len(self.motor.audición.comandos_en_cola)
            }
        return {"audición": "no_disponible"}
    
    def ver_historial(self, últimos: int = 10) -> List[Dict]:
        """Ver historial de operaciones"""
        return self.historial[-últimos:]
    
    def diagnosticar(self) -> Dict[str, Any]:
        """Ejecutar diagnóstico del avatar"""
        if self.motor:
            return self.motor.diagnosticar()
        return {"diagnóstico": "no_disponible"}
    
    def ver_estadísticas(self) -> Dict[str, Any]:
        """Ver estadísticas de operación"""
        if self.motor:
            return self.motor.ver_estadísticas()
        return {"estadísticas": "no_disponible"}
    
    def ayuda(self) -> str:
        """Mostrar ayuda de comandos"""
        ayuda = f"""
        ╔════════════════════════════════════════════════════════════════╗
        ║           🤖 AVATAR {self.nombre_avatar} - SISTEMA DE AYUDA             ║
        ╠════════════════════════════════════════════════════════════════╣
        ║                                                                ║
        ║  COMANDOS DISPONIBLES:                                        ║
        ║                                                                ║
        ║  1. ejecutar_comando(cmd)  → Ejecutar comando                 ║
        ║  2. ver_estado()           → Ver estado del avatar            ║
        ║  3. ver_pantalla_interna() → Ver pantalla de creación         ║
        ║  4. ver_visión()           → Ver análisis visual              ║
        ║  5. ver_audición()         → Ver estado de audición           ║
        ║  6. ver_historial()        → Ver últimas operaciones          ║
        ║  7. diagnosticar()         → Diagnóstico completo             ║
        ║  8. ver_estadísticas()     → Ver estadísticas                 ║
        ║  9. ayuda()                → Esta ayuda                       ║
        ║                                                                ║
        ║  EJEMPLOS:                                                     ║
        ║  interfaz.ejecutar_comando("analizar código")                 ║
        ║  interfaz.ver_estado()                                        ║
        ║  interfaz.ver_pantalla_interna()                              ║
        ║                                                                ║
        ╚════════════════════════════════════════════════════════════════╝
        """
        return ayuda


def demostración():
    """Demostración interactiva del avatar"""
    print("\n" + "="*60)
    print("🎯 DEMOSTRACIÓN INTERACTIVA - AVATAR ARIA")
    print("="*60 + "\n")
    
    # Crear interfaz
    interfaz = InterfazAvatar("ARIA")
    
    # Mostrar ayuda
    print(interfaz.ayuda())
    
    # Opciones de demostración
    print("\nOPCIONES DE DEMOSTRACIÓN:\n")
    print("1. Ver estado del avatar")
    print("2. Ejecutar comando de análisis")
    print("3. Ver pantalla interna")
    print("4. Diagnosticar sistema")
    print("5. Ver estadísticas")
    print("0. Salir\n")
    
    opción = input("Selecciona una opción (0-5): ").strip()
    
    if opción == "1":
        print("\n📊 ESTADO DEL AVATAR:")
        print(json.dumps(interfaz.ver_estado(), indent=2, ensure_ascii=False))
    
    elif opción == "2":
        comando = input("\nIngresa comando: ")
        print(f"\n🔄 Ejecutando: {comando}")
        resultado = interfaz.ejecutar_comando(comando)
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
    
    elif opción == "3":
        print("\n🎨 PANTALLA INTERNA:")
        print(json.dumps(interfaz.ver_pantalla_interna(), indent=2, ensure_ascii=False))
    
    elif opción == "4":
        print("\n🔍 DIAGNÓSTICO:")
        print(json.dumps(interfaz.diagnosticar(), indent=2, ensure_ascii=False))
    
    elif opción == "5":
        print("\n📈 ESTADÍSTICAS:")
        print(json.dumps(interfaz.ver_estadísticas(), indent=2, ensure_ascii=False))
    
    elif opción == "0":
        print("\n👋 Hasta luego!")
        sys.exit(0)


if __name__ == "__main__":
    demostración()

package com.example.order.architecture;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.noClasses;

import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.core.importer.ImportOption;
import org.junit.jupiter.api.Test;

class LayeredArchitectureTest {

    private final JavaClasses importedClasses =
        new ClassFileImporter()
            .withImportOption(ImportOption.Predefined.DO_NOT_INCLUDE_TESTS)
            .importPackages("com.example.order");

    @Test
    void controller_does_not_depend_on_repository() {
        noClasses()
            .that().resideInAPackage("..controller..")
            .should().dependOnClassesThat().resideInAPackage("..repository..")
            .check(importedClasses);
    }

    @Test
    void service_does_not_depend_on_controller() {
        noClasses()
            .that().resideInAPackage("..service..")
            .should().dependOnClassesThat().resideInAPackage("..controller..")
            .check(importedClasses);
    }

    @Test
    void domain_does_not_depend_on_application_layers() {
        noClasses()
            .that().resideInAPackage("..domain..")
            .should().dependOnClassesThat().resideInAnyPackage(
                "..controller..",
                "..service..",
                "..repository.."
            )
            .check(importedClasses);
    }
}

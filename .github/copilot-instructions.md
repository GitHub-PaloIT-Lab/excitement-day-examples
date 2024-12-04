Always use the hungarian notation prefix for the following items:

- Parameters: Prefix with par. For example, parLocation.
- Variables: Prefix with var. For example, varStorageAccountName.
- Resources: Prefix with res. For example, resStorageAccount.
- Modules: Prefix with mod. For example, modStorageAccount.
- Outputs: Prefix with out. For example, outStorageAccountName.
- User-Defined Functions: Prefix with func. For example, funcMyFunctionHere.
- User-Defined Types: Prefix with type. For example, typeMyTypeHere.

When using the existing keyword to refer to resources, append `Ref` to the symbolic name of each resource. For instance, if referencing an existing storage account, use the format `resExistingStorageAccountRef`.

If a parameter name includes ‘password,’ ‘admin,’ or ‘key,’ apply the @secure decorator to ensure secure handling. For example, use `@secure` with parameters like adminPassword or apiKey.

Always add a description decorator `@description` on parameters and outputs to describe the purpose. If the parameter is required, start the description with `Required.` and when the parameter is optional or nullable start with `Optional.`.

Begin module names with the format deploy-resource-type-${resource-type-name}. For example, in a Key Vault deployment:

```bicep
@description('Required. The name of the Key Vault.')
param parKeyVaultName string

module modKeyVault 'br/public:avm/res/key-vault/vault:0.9.0' = {
  name: 'deploy-key-vault-${parKeyVaultName}'
  params: {
    name: parKeyVaultName
    location: parLocation
  }
}
```
Every time i create a new markdown file in english, please translate it to italian. Put this translation in a new file, with the same filenmae but prefixed wit it_
